import asyncio
import os
import warnings
from typing import List, Optional
from pathlib import Path

import numpy as np
from pydantic import SecretStr

# LangChain 相关导入
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
# 替换这行导入
# from langchain_huggingface import HuggingFaceEmbeddings

# 改为：
from langchain_community.embeddings import HuggingFaceEmbeddings
# 你的模式定义
from schemas.agent import NameResultSchema
from schemas.name import NameIn

# 设置环境变量来禁用不必要的警告
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
warnings.filterwarnings("ignore", category=UserWarning, module="huggingface_hub")


# ==================== 配置部分 ====================

class Config:
    """配置类"""
    # PDF知识库路径（支持多个PDF文件）
    PDF_PATHS = [
        "classical_literature.pdf",
        "tang_poetry.pdf",
        "chu_ci.pdf",
        "论语.pdf",
        "唐诗三百首.pdf"
    ]

    # 嵌入模型配置
    EMBEDDING_MODEL = "BAAI/bge-small-zh"
    DEVICE = "cpu"  # 使用cpu或cuda

    # RAG检索配置
    TOP_K = 5  # 检索最相关的K个片段
    CHUNK_SIZE = 500  # 文本分块大小
    CHUNK_OVERLAP = 50  # 分块重叠大小

    # LLM配置（保持你的原配置）
    LLM_MODEL = "qwen-plus"
    LLM_API_KEY = "sk-4bf1bf6da432483fb41db969e8ebe9c2"
    LLM_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    # 系统提示（保持你的原系统提示）
    SYSTEM_PROMPT = """你是一位精通汉语言文学、音韵学与传统文化的命名专家，擅长为人物创作兼具音律美感、深刻寓意与文化内涵的姓名。请严格遵循以下原则进行命名：

发音优先：名字需平仄协调、声调起伏自然，避免拗口、谐音歧义（如不雅谐音、负面联想），朗朗上口，富有韵律感；
寓意深远：结合用户提供的背景（如姓氏、性别、字数和其他要求等），选取具有积极象征意义的意象（如自然元素、美德品质、经典典故），做到"名以载道"；
内涵厚重：优先从《诗经》《楚辞》《论语》等经典文献，或唐诗宋词、成语典故中汲取灵感，确保名字有出处、有底蕴，避免空洞堆砌；
现代适配：在尊重传统的基础上，兼顾当代语境与审美，避免过度古奥或生僻字（生僻字需附注音与释义），确保实用性与传播性；
个性化定制：根据用户具体需求（如性别倾向、字数限制、风格偏好——儒雅/清丽/大气/灵动等），提供5个候选方案，并按照以下格式输出：
【姓名】姓名
【出处】典籍来源或文化意象
【寓意】字义拆解与整体象征"""


# ==================== RAG核心模块 ====================

class PDFKnowledgeBase:
    """PDF知识库管理类"""

    def __init__(self, config: Config):
        self.config = config
        self.embeddings = HuggingFaceEmbeddings(
            model_name=config.EMBEDDING_MODEL,
            model_kwargs={'device': config.DEVICE},
            encode_kwargs={'normalize_embeddings': True}
        )
        self.documents: List[str] = []
        self.document_embeddings: Optional[np.ndarray] = None

    def load_pdfs(self) -> List[str]:
        """加载所有PDF文档"""
        all_texts = []

        for pdf_path in self.config.PDF_PATHS:
            if not os.path.exists(pdf_path):
                print(f"警告: PDF文件不存在，跳过: {pdf_path}")
                continue

            try:
                from pypdf import PdfReader
                reader = PdfReader(pdf_path)
                print(f"正在加载: {pdf_path} (共{len(reader.pages)}页)")

                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text and text.strip():
                        # 对长文本进行分块
                        chunks = self._chunk_text(text.strip())
                        all_texts.extend(chunks)

            except ImportError:
                print(f"错误: 请安装pypdf库: pip install pypdf")
                return []
            except Exception as e:
                print(f"读取PDF {pdf_path} 时出错: {e}")

        print(f"知识库加载完成，共 {len(all_texts)} 个文本片段")
        return all_texts

    def _chunk_text(self, text: str) -> List[str]:
        """将长文本分割成小块"""
        chunks = []
        words = text.split()

        for i in range(0, len(words), self.config.CHUNK_SIZE - self.config.CHUNK_OVERLAP):
            chunk = " ".join(words[i:i + self.config.CHUNK_SIZE])
            if chunk:
                chunks.append(chunk)
            if i + self.config.CHUNK_SIZE >= len(words):
                break

        return chunks if chunks else [text[:500]]  # 确保至少返回一个片段

    def build_index(self):
        """构建文档索引（计算向量）"""
        if not self.documents:
            # 如果没有PDF文件，使用默认的示例知识库
            self.documents = self._get_default_knowledge()
            print("使用内置示例知识库")

        print("正在构建向量索引...")

        # 为所有文档计算向量
        doc_vectors = []
        for i, doc in enumerate(self.documents):
            vector = self.embeddings.embed_query(doc)
            doc_vectors.append(vector)

            if (i + 1) % 50 == 0:
                print(f"已处理 {i + 1}/{len(self.documents)} 个文档片段")

        self.document_embeddings = np.array(doc_vectors)
        print(f"向量索引构建完成，维度: {self.document_embeddings.shape}")

    def retrieve(self, query: str, k: Optional[int] = None) -> List[str]:
        """检索与查询最相关的文档片段"""
        if k is None:
            k = self.config.TOP_K

        if self.document_embeddings is None or len(self.documents) == 0:
            return ["知识库为空，将基于通用文化知识生成名字。"]

        # 计算查询向量
        query_vector = self.embeddings.embed_query(query)

        # 计算余弦相似度（向量已归一化，直接点积）
        similarities = np.dot(self.document_embeddings, query_vector)

        # 获取最相关的k个片段
        top_indices = np.argsort(similarities)[-k:][::-1]

        # 构建检索结果
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.3:  # 相似度阈值
                results.append(self.documents[idx])

        if not results:
            return ["未找到高度相关的文献，将结合通用知识生成。"]

        return results

    def _get_default_knowledge(self) -> List[str]:
        """获取默认知识库（当PDF不存在时使用）"""
        return [
            # 《诗经》经典
            "《诗经·关雎》：关关雎鸠，在河之洲。窈窕淑女，君子好逑。",
            "《诗经·桃夭》：桃之夭夭，灼灼其华。之子于归，宜其室家。",
            "《诗经·蒹葭》：蒹葭苍苍，白露为霜。所谓伊人，在水一方。",
            "《诗经·淇奥》：有匪君子，如切如磋，如琢如磨。",

            # 《楚辞》经典
            "《楚辞·离骚》：路漫漫其修远兮，吾将上下而求索。",
            "《楚辞·九歌》：青云衣兮白霓裳，举长矢兮射天狼。",
            "《楚辞·涉江》：余幼好此奇服兮，年既老而不衰。",

            # 唐诗名句
            "李白《清平调》：云想衣裳花想容，春风拂槛露华浓。",
            "王维《山居秋暝》：明月松间照，清泉石上流。",
            "杜甫《春望》：国破山河在，城春草木深。",
            "李商隐《锦瑟》：沧海月明珠有泪，蓝田日暖玉生烟。",

            # 宋词名句
            "苏轼《水调歌头》：明月几时有，把酒问青天。",
            "李清照《声声慢》：寻寻觅觅，冷冷清清，凄凄惨惨戚戚。",
            "辛弃疾《青玉案》：众里寻他千百度，蓦然回首，那人却在灯火阑珊处。",

            # 《论语》经典
            "《论语·学而》：学而时习之，不亦说乎？有朋自远方来，不亦乐乎？",
            "《论语·雍也》：知者乐水，仁者乐山。知者动，仁者静。知者乐，仁者寿。",

            # 命名常用意象
            "玉：象征纯洁、高贵、温润，常用于女性名字，如黛玉、玉环。",
            "兰：象征高洁、优雅、芬芳，如兰心、蕙兰。",
            "竹：象征正直、坚韧、虚心，如竹君、筠竹。",
            "云：象征自由、飘逸、高远，如云舒、云逸。",
            "月：象征纯洁、美丽、思念，如月华、秋月。",

            # 音韵学知识
            "平仄协调：名字的声调应平仄相间，避免全平或全仄，如'张华'（平平）不如'张晔'（平仄）。",
            "避免谐音：注意名字的谐音联想，如'范统'（饭桶）、'杜子腾'（肚子疼）应避免。",

            # 性别用字倾向
            "女性常用字：婉、静、雅、淑、慧、芳、婷、妍、娇、娜、媛、姝、莹、蕊",
            "男性常用字：伟、强、俊、杰、斌、浩、宇、辰、轩、睿、博、文、武、毅",

            # 古典名字示例
            "王维（字摩诘）：取自佛教经典，寓意清净智慧。",
            "白居易（字乐天）：'居易'出自《中庸》，'乐天'体现达观性格。",
            "李清照：'清照'寓意清澈明亮，与其词风相称。",
            "苏东坡：'东坡'取自黄州东坡，体现豁达情怀。"
        ]


# ==================== 主应用类 ====================

class NamingAssistant:
    """命名助手主类"""

    def __init__(self):
        self.config = Config()

        # 初始化LLM（保持你的原配置）
        self.llm = ChatOpenAI(
            model=self.config.LLM_MODEL,
            api_key=SecretStr("sk-df3970f7b5264348800fc7e3c0cff56b"),
            temperature=1,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

        # 初始化知识库
        self.knowledge_base = PDFKnowledgeBase(self.config)
        self.knowledge_base.load_pdfs()
        self.knowledge_base.build_index()

        # 初始化Agent（保持你的原配置）
        self.agent = create_agent(
            model=self.llm,
            system_prompt=self.config.SYSTEM_PROMPT,
            response_format=NameResultSchema
        )

    async def generate_names(self, name_info: NameIn) -> NameResultSchema:
        """生成名字（RAG增强版本）"""

        # 1. 构建查询
        query_parts = [
            f"姓氏：{name_info.surname}",
            f"性别：{name_info.gender}",
            f"字数：{name_info.length}"
        ]

        if name_info.other:
            query_parts.append(f"要求：{name_info.other}")
        if name_info.exclude:
            query_parts.append(f"排除：{'、'.join(name_info.exclude)}")

        query = " ".join(query_parts)

        # 2. 从知识库检索相关内容
        print("正在从知识库检索相关信息...")
        relevant_docs = self.knowledge_base.retrieve(query)

        # 3. 构建增强提示
        rag_context = "\n".join([f"- {doc}" for doc in relevant_docs[:3]])  # 取最相关的3条

        enhanced_prompt = f"""
{query}

相关文献参考：
{rag_context}

请基于以上信息，严格按照要求生成名字。
"""

        # 4. 调用Agent生成结果（保持你的原调用方式）
        print("正在生成名字...")
        result = await self.agent.ainvoke({
            "messages": [{"role": "user", "content": enhanced_prompt}]
        })

        return result['structured_response']

    def get_knowledge_stats(self) -> dict:
        """获取知识库统计信息"""
        return {
            "document_count": len(self.knowledge_base.documents),
            "has_pdfs": any(os.path.exists(p) for p in self.config.PDF_PATHS),
            "vector_dim": self.knowledge_base.document_embeddings.shape[1]
            if self.knowledge_base.document_embeddings is not None else 0
        }


# ==================== 主程序 ====================

async def main():
    """主程序"""
    print("=" * 60)
    print("命名助手 - RAG增强版")
    print("=" * 60)

    # 初始化助手
    print("\n初始化命名助手...")
    assistant = NamingAssistant()

    # 显示知识库状态
    stats = assistant.get_knowledge_stats()
    print(f"知识库状态：{stats['document_count']} 个文本片段")
    if not stats['has_pdfs']:
        print("提示：未检测到PDF文件，使用内置示例知识库")
        print("请将PDF文件放置在以下位置之一：")
        for path in assistant.config.PDF_PATHS[:3]:
            print(f"  - {path}")

    # 测试用例1（你的原测试用例）
    print("\n" + "=" * 40)
    print("测试用例1：为张姓女孩起两字名")
    print("=" * 40)

    name_info = NameIn(
        surname="张",
        gender='女',
        length="两字",
        other="风格清丽，有文学气息",
        exclude=[]
    )

    try:
        result = await assistant.generate_names(name_info)
        print("\n生成结果：")
        print(result)
    except Exception as e:
        print(f"生成名字时出错: {e}")
        import traceback
        traceback.print_exc()

    # 测试用例2（可选，展示更多功能）
    print("\n" + "=" * 40)
    print("测试用例2：为李姓男孩起三字名")
    print("=" * 40)

    name_info2 = NameIn(
        surname="李",
        gender='男',
        length="两字",
        other="大气磅礴，有志向远大之意",
        exclude=["李建国", "李向阳"]
    )

    try:
        result2 = await assistant.generate_names(name_info2)
        print("\n生成结果：")
        print(result2)
    except Exception as e:
        print(f"生成名字时出错: {e}")


if __name__ == '__main__':
    # 运行主程序
    asyncio.run(main())
