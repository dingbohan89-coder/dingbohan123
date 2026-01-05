# Claude Social Media Scraper Skills

为 Claude Code 设计的社交媒体爬虫技能包，支持抓取小红书和 TikTok 的公开内容。

**GitHub 仓库：** https://github.com/luoxikang/modulon-labs-tkskills

> **💡 快速开始提示：** 推荐在 **Git Bash** 中使用 Claude Code 以获得最佳兼容性。详见下方安装说明。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-%3E=16.0.0-green)](https://nodejs.org/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-blue)](https://claude.ai/claude-code)

## 📦 包含的技能

- **xiaohongshu-skill** - 小红书帖子爬虫
- **tiktok-skill** - TikTok 视频爬虫

## ✨ 功能特性

### 小红书爬虫 (xiaohongshu-skill)
- ✅ 抓取帖子标题、正文内容、作者信息
- ✅ 提取互动数据（点赞、收藏、评论、分享）
- ✅ 支持图文笔记完整内容
- ⚠️ 视频笔记仅获取标签信息

### TikTok 爬虫 (tiktok-skill)
- ✅ 抓取视频标题、描述、作者信息
- ✅ 提取互动数据（点赞、评论、分享、收藏）
- ✅ 提取话题标签（hashtags）
- ⚠️ 播放量仅作者可见，无法提取

## 🚀 一键安装（推荐）

### ⚠️ 重要提示：使用 Git Bash

**强烈推荐在 Git Bash 中使用 Claude Code**

如果你的系统终端与 Claude Code 不兼容（如 Windows CMD），请：
1. 安装 [Git for Windows](https://git-scm.com/download/win)（包含 Git Bash）
2. 打开 **Git Bash** 终端
3. 在 Git Bash 中启动和使用 Claude Code

**为什么使用 Git Bash？**
- ✅ 完美兼容 Claude Code 内置工具
- ✅ 支持 Unix 风格命令（`~`, `&&`, 等）
- ✅ 跨平台一致性好
- ✅ 避免路径转义问题

### 支持的平台

✅ Claude Code CLI（推荐在 Git Bash 中使用）
✅ Claude Code 桌面版
✅ Cursor IDE (内置 Claude Code)

### 方法 1: 使用 Claude Code 自动配置 ⭐

**根据你的平台选择对应的提示词：**

#### 📌 Claude Code CLI / 桌面版

在 Claude Code 中输入：

```
请帮我安装社交媒体爬虫技能包：

1. 从 GitHub 克隆仓库到我的用户主目录：
   git clone https://github.com/luoxikang/modulon-labs-tkskills.git ~/claude_skills

2. 安装 Node.js 依赖：
   cd ~/claude_skills/xiaohongshu-skill && npm install
   cd ~/claude_skills/tiktok-skill && npm install

3. 安装 Playwright 浏览器：
   cd ~/claude_skills && npx playwright install chromium

4. 配置 Claude Code：
   - 找到或创建配置文件：
     * Windows: C:\Users\你的用户名\.claude\settings.json
     * macOS: ~/.claude/settings.json
     * Linux: ~/.claude/settings.json
   - 添加以下内容（使用实际完整路径）：
     {
       "skillsPath": "完整路径/claude_skills"
     }

5. 完成后告诉我，我会重启 Claude Code
```

#### 📌 Cursor IDE

在 Cursor 中输入：

```
请帮我安装社交媒体爬虫技能包：

1. 从 GitHub 克隆仓库：
   git clone https://github.com/luoxikang/modulon-labs-tkskills.git ~/claude_skills

2. 安装 Node.js 依赖：
   cd ~/claude_skills/xiaohongshu-skill && npm install
   cd ~/claude_skills/tiktok-skill && npm install

3. 安装 Playwright 浏览器：
   cd ~/claude_skills && npx playwright install chromium

4. 配置 Cursor 的 Claude Code：
   - 找到或创建 Cursor 配置文件：
     * Windows: %APPDATA%\Cursor\User\settings.json
     * macOS: ~/Library/Application Support/Cursor/User/settings.json
   - 添加以下内容（使用实际完整路径）：
     {
       "claude-code.skillsPath": "完整路径/claude_skills"
     }

5. 完成后告诉我，我会重启 Cursor
```

### 方法 2: 手动安装

#### 前置要求

确保已安装：
- **Node.js** v16+ - [下载地址](https://nodejs.org/)
- **Claude Code** (CLI/桌面版) 或 **Cursor IDE**
- **Git** - [下载地址](https://git-scm.com/)

#### 安装步骤

**1. 克隆项目**

```bash
# 使用 Git 克隆
git clone https://github.com/luoxikang/modulon-labs-tkskills.git

# 或下载 ZIP 并解压
```

**2. 安装依赖**

```bash
# 小红书爬虫依赖
cd claude_skills/xiaohongshu-skill
npm install

# TikTok 爬虫依赖
cd ../tiktok-skill
npm install
```

**3. 安装浏览器（仅需执行一次）**

```bash
# 在任一技能目录中运行
npx playwright install chromium
```

**4. 根据平台配置**

##### Claude Code CLI / 桌面版

找到或创建配置文件：
- **Windows**: `C:\Users\你的用户名\.claude\settings.json`
- **macOS**: `~/.claude/settings.json`
- **Linux**: `~/.claude/settings.json`

添加以下内容：

```json
{
  "skillsPath": "你的完整路径/claude_skills"
}
```

**路径示例：**
- Windows: `"E:/claude_skills"`
- macOS: `"/Users/你的名字/claude_skills"`
- Linux: `"/home/你的名字/claude_skills"`

##### Cursor IDE

找到或创建 Cursor 配置文件：
- **Windows**: `%APPDATA%\Cursor\User\settings.json`
- **macOS**: `~/Library/Application Support/Cursor/User/settings.json`
- **Linux**: `~/.config/Cursor/User/settings.json`

添加以下内容：

```json
{
  "claude-code.skillsPath": "你的完整路径/claude_skills"
}
```

**5. 重启应用**

完全关闭并重新启动：
- Claude Code CLI/桌面版
- 或 Cursor IDE

**6. 验证安装**

在 Claude Code 中询问：
```
What skills are available?
```

你应该能看到 `xiaohongshu-skill` 和 `tiktok-skill`。

## 🔑 首次登录

安装完成后，需要登录相应平台才能抓取内容。

### 小红书登录

```bash
cd claude_skills/xiaohongshu-skill
node scripts/manual-login.js
```

- 浏览器会自动打开小红书首页
- 手动完成登录（扫码或手机号）
- 登录成功后，访问几个帖子页面
- 按 `Ctrl+C`（macOS: `Cmd+C`）保存登录状态

### TikTok 登录

```bash
cd claude_skills/tiktok-skill
node scripts/login.js
```

- 浏览器会自动打开 TikTok
- 手动完成登录
- 按 `Ctrl+C` 保存登录状态

## 📖 使用方法

### 在 Claude Code 中使用

**爬取小红书帖子：**
```
请爬取这个小红书帖子：https://www.xiaohongshu.com/discovery/item/695a0e81000000001e00c245
```

**爬取 TikTok 视频：**
```
请爬取这个 TikTok 视频：https://www.tiktok.com/@username/video/1234567890
```

### 直接运行脚本

**小红书：**
```bash
cd claude_skills/xiaohongshu-skill
node scripts/scrape.js "帖子URL"
```

**TikTok：**
```bash
cd claude_skills/tiktok-skill
node scripts/scrape.js "视频URL"
```

### 查看结果

爬取结果保存在各技能的 `results/` 目录下：
- 小红书: `xiaohongshu-skill/results/xhs_post_时间戳.json`
- TikTok: `tiktok-skill/results/tiktok_video_时间戳.json`

## 📁 项目结构

```
claude_skills/
├── README.md                           # 本文件
├── .gitignore                          # Git 忽略文件
├── LICENSE                             # MIT 许可证
├── AUTO_SETUP_PROMPT.md                # 自动配置提示词
├── xiaohongshu-skill/                  # 小红书爬虫
│   ├── SKILL.md                        # 技能定义文件（必需）
│   ├── package.json                    # 依赖配置
│   ├── scripts/
│   │   ├── manual-login.js            # 登录助手
│   │   ├── scrape.js                  # 主爬虫
│   │   ├── scrape-human.js            # 人工模式
│   │   └── scrape-stealth.js          # 隐身模式
│   ├── results/                        # 爬取结果（自动生成）
│   └── xhs_cookies.json               # 登录状态（自动生成）
└── tiktok-skill/                       # TikTok 爬虫
    ├── SKILL.md                        # 技能定义文件（必需）
    ├── package.json                    # 依赖配置
    ├── scripts/
    │   ├── login.js                   # 登录助手
    │   ├── scrape.js                  # 主爬虫
    │   └── get-stats.js               # 统计提取
    ├── results/                        # 爬取结果（自动生成）
    └── tiktok_cookies.json            # 登录状态（自动生成）
```

## 🛠️ 故障排除

### 问题：登录状态过期

**症状：** 爬取失败或显示"无法浏览"

**解决方法：**
```bash
# 删除旧 cookies
rm xiaohongshu-skill/xhs_cookies.json
rm tiktok-skill/tiktok_cookies.json

# 重新登录
cd xiaohongshu-skill && node scripts/manual-login.js
cd ../tiktok-skill && node scripts/login.js
```

### 问题：技能未显示

**检查清单：**
- [ ] `SKILL.md` 文件是否存在
- [ ] 配置文件路径是否正确
- [ ] 是否已重启应用
- [ ] JSON 格式是否正确（注意逗号和引号）

**平台特定配置文件位置：**

| 平台 | 配置文件路径 |
|------|-------------|
| Claude Code CLI (Windows) | `C:\Users\用户名\.claude\settings.json` |
| Claude Code CLI (macOS) | `~/.claude/settings.json` |
| Claude Code 桌面版 | 与 CLI 相同 |
| Cursor (Windows) | `%APPDATA%\Cursor\User\settings.json` |
| Cursor (macOS) | `~/Library/Application Support/Cursor/User/settings.json` |

### 问题：浏览器未安装

**错误信息：** `Executable doesn't exist`

**解决方法：**
```bash
npx playwright install chromium
```

### 问题：依赖安装失败

**解决方法：**
```bash
# 清理缓存
npm cache clean --force

# 删除 node_modules 重新安装
rm -rf node_modules
npm install
```

### 问题：Cursor 中技能不生效

**解决方法：**
1. 确认配置文件是 `settings.json` 而非 `claude-code.json`
2. 配置项应为 `claude-code.skillsPath`
3. 确保 Cursor 已重启
4. 检查 Cursor 设置是否启用了 Claude Code 技能

## 🌟 不同平台使用提示

### Claude Code CLI
- 配置文件：`~/.claude/settings.json`
- 直接在终端使用，适合自动化脚本
- 支持所有 Claude Code 功能

### Claude Code 桌面版
- 配置文件：与 CLI 共享 `~/.claude/settings.json`
- 图形界面，更友好的交互体验
- 适合日常使用

### Cursor IDE
- 配置文件：`~/Library/Application Support/Cursor/User/settings.json` (macOS)
- 配置项前缀：`claude-code.`
- 深度集成 IDE 功能
- 可能需要额外启用 Claude Code 插件

## ⚠️ 重要说明

### 法律与道德

1. **仅供学习研究** - 请勿用于商业用途
2. **遵守平台规则** - 不要大规模或高频抓取
3. **尊重原创** - 使用数据时注明出处
4. **控制频率** - 建议每次请求间隔 5 秒以上
5. **隐私保护** - 只抓取公开内容

### 技术限制

1. **登录状态会过期** - cookies 通常 7-30 天失效
2. **平台可能更新** - 网页结构变化可能导致爬虫失效
3. **反爬虫机制** - 频繁请求可能被限制或封禁
4. **数据不完整** - 某些数据（如播放量）无法获取

### 数据准确性

- 小红书视频笔记仅获取标签，不含视频内容
- TikTok 播放量仅作者可见
- 评论/分享数有时无法提取
- 数值格式可能不统一（如 "1.3万" vs "13000"）

## 🔧 技术细节

### 技术栈
- **Node.js** v16+ - JavaScript 运行环境
- **Playwright** - 浏览器自动化框架
- **Chromium** - 无头浏览器

### 工作原理
1. 加载已保存的登录 cookies
2. 使用真实浏览器访问目标 URL
3. 等待页面完全加载（20-30 秒）
4. 从页面 DOM 或嵌入的 JSON 中提取数据
5. 保存结果到本地 JSON 文件
6. 更新 cookies 以备下次使用

### 为什么使用浏览器模拟？

- ✅ 动态内容需要 JavaScript 渲染
- ✅ 绕过基本的反爬虫检测
- ✅ 支持登录状态和会话管理
- ✅ 更接近真实用户行为

## 📝 更新日志

### v1.0.0 (2025-01-05)
- 🎉 初始版本发布
- ✨ 支持小红书和 TikTok 基础爬取
- 📚 完整文档和配置说明
- 🤖 支持 Claude Code CLI/桌面版/Cursor
- 🚀 提供自动化配置提示词

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

**仓库地址：** https://github.com/luoxikang/modulon-labs-tkskills

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## ⚖️ 免责声明

本工具仅供技术学习和研究使用。使用者应当：
- 遵守相关平台的服务条款和使用协议
- 遵守当地法律法规
- 尊重原创者的知识产权
- 不将数据用于商业或非法目的
- 自行承担使用本工具的风险和责任

作者不对本工具的使用方式或后果负责。

## 🔗 相关链接

- **Claude Code 官网**: https://claude.ai/claude-code
- **Cursor IDE**: https://cursor.sh
- **问题反馈**: https://github.com/luoxikang/modulon-labs-tkskills/issues

---

**享受使用 Claude Code 爬取社交媒体内容吧！** 🎉

如有问题，请查看[故障排除](#-故障排除)部分或提交 Issue。
