# 自动配置提示词

## ⚠️ 重要：使用 Git Bash

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

---

## 🎯 选择你的平台

### 1️⃣ Claude Code CLI 或桌面版

**适用场景：**
- 使用 Claude Code 命令行工具
- 使用 Claude Code 桌面应用程序

**复制以下提示词到 Claude Code：**

```
请帮我安装社交媒体爬虫技能包：

1. 从 GitHub 克隆仓库到我的用户主目录：
   git clone https://github.com/luoxikang/modulon-labs-tkskills.git ~/claude_skills

2. 检查并安装 Node.js 依赖：
   cd ~/claude_skills/xiaohongshu-skill && npm install
   cd ~/claude_skills/tiktok-skill && npm install

3. 安装 Playwright 浏览器：
   cd ~/claude_skills/xiaohongshu-skill && npx playwright install chromium

4. 配置 Claude Code：
   - 读取或创建配置文件 ~/.claude/settings.json
   - 添加以下内容（使用实际的完整路径替换"完整路径"）：
     {
       "skillsPath": "完整路径/claude_skills"
     }
   注意：Windows 用户路径为 C:\Users\用户名\.claude\settings.json

5. 验证配置：列出配置文件内容，确认 skillsPath 已正确设置

6. 完成后告诉我步骤和结果，我会重启 Claude Code
```

---

### 2️⃣ Cursor IDE

**适用场景：**
- 使用 Cursor 编辑器
- 在 Cursor 中使用 Claude Code 集成

**复制以下提示词到 Cursor：**

```
请帮我安装社交媒体爬虫技能包：

1. 从 GitHub 克隆仓库：
   git clone https://github.com/luoxikang/modulon-labs-tkskills.git ~/claude_skills

2. 检查并安装 Node.js 依赖：
   cd ~/claude_skills/xiaohongshu-skill && npm install
   cd ~/claude_skills/tiktok-skill && npm install

3. 安装 Playwright 浏览器：
   cd ~/claude_skills/xiaohongshu-skill && npx playwright install chromium

4. 配置 Cursor 的 Claude Code：
   - 读取或创建 Cursor 配置文件：
     * Windows: %APPDATA%\Cursor\User\settings.json
     * macOS: ~/Library/Application Support/Cursor/User/settings.json
     * Linux: ~/.config/Cursor/User/settings.json
   - 添加以下内容（使用实际的完整路径替换"完整路径"）：
     {
       "claude-code.skillsPath": "完整路径/claude_skills"
     }

5. 验证配置：列出配置文件内容，确认 claude-code.skillsPath 已正确设置

6. 完成后告诉我步骤和结果，我会重启 Cursor
```

---

## 📖 使用说明

### Claude Code 会自动执行的操作

当你输入提示词后，Claude 会：

✅ 克隆 GitHub 仓库
✅ 安装所有 Node.js 依赖（playwright, puppeteer 等）
✅ 安装 Chromium 浏览器
✅ 创建或更新配置文件
✅ 设置正确的 skillsPath
✅ 验证配置是否成功

### 配置完成后的操作

当 Claude 告诉你配置完成后：

1. **重启应用**
   - Claude Code CLI/桌面版：完全关闭并重新打开
   - Cursor IDE：完全关闭并重新打开

2. **验证安装**

   在 Claude Code 中输入：
   ```
   What skills are available?
   ```

3. **开始使用**

   你应该能看到：
   - `xiaohongshu-skill` - 小红书爬虫
   - `tiktok-skill` - TikTok 爬虫

---

## 🔧 自定义安装路径

如果你想安装到其他目录，修改提示词中的路径：

### Windows 示例

**Claude Code CLI/桌面版：**
```
git clone https://github.com/luoxikang/modulon-labs-tkskills.git E:\claude-skills
```

配置：
```json
{
  "skillsPath": "E:/claude-skills"
}
```

**Cursor IDE：**
```
git clone https://github.com/luoxikang/modulon-labs-tkskills.git E:\claude-skills
```

配置：
```json
{
  "claude-code.skillsPath": "E:/claude-skills"
}
```

### macOS/Linux 示例

**Claude Code CLI/桌面版：**
```
git clone https://github.com/luoxikang/modulon-labs-tkskills.git /opt/claude-skills
```

配置：
```json
{
  "skillsPath": "/opt/claude-skills"
}
```

**Cursor IDE：**
```
git clone https://github.com/luoxikang/modulon-labs-tkskills.git /opt/claude-skills
```

配置：
```json
{
  "claude-code.skillsPath": "/opt/claude-skills"
}
```

---

## 📍 配置文件路径参考

### Claude Code CLI / 桌面版

| 操作系统 | 配置文件路径 |
|---------|-------------|
| Windows | `C:\Users\用户名\.claude\settings.json` |
| macOS | `~/.claude/settings.json` |
| Linux | `~/.claude/settings.json` |

**配置项：** `skillsPath`

### Cursor IDE

| 操作系统 | 配置文件路径 |
|---------|-------------|
| Windows | `%APPDATA%\Cursor\User\settings.json` |
| macOS | `~/Library/Application Support/Cursor/User/settings.json` |
| Linux | `~/.config/Cursor/User/settings.json` |

**配置项：** `claude-code.skillsPath`

---

## ⚠️ 常见问题

### 问题：Claude 无法访问 GitHub

**解决方法：** 手动下载 ZIP 文件并解压，然后使用修改后的提示词：

**Claude Code CLI/桌面版：**
```
请帮我配置社交媒体爬虫技能包，文件已下载到：~/Downloads/claude_skills

请执行以下步骤：
1. cd ~/claude_skills/xiaohongshu-skill && npm install
2. cd ~/claude_skills/tiktok-skill && npm install
3. 配置 ~/.claude/settings.json，设置 skillsPath
...
```

**Cursor IDE：**
```
请帮我配置社交媒体爬虫技能包，文件已下载到：~/Downloads/claude_skills

请执行以下步骤：
1. cd ~/claude_skills/xiaohongshu-skill && npm install
2. cd ~/claude_skills/tiktok-skill && npm install
3. 配置 Cursor 的 settings.json，设置 claude-code.skillsPath
...
```

### 问题：npm install 失败

**Claude 会自动尝试：**
- 清理 npm 缓存
- 删除 node_modules
- 重新安装依赖

**如果仍然失败，检查：**
- Node.js 版本是否 >= 16
- 网络连接是否正常
- 是否有足够的磁盘空间

### 问题：配置文件路径错误

**Claude Code CLI/桌面版会自动检测：**
- Windows: `C:\Users\用户名\.claude\settings.json`
- macOS/Linux: `~/.claude/settings.json`

**Cursor IDE 会自动检测：**
- Windows: `%APPDATA%\Cursor\User\settings.json`
- macOS: `~/Library/Application Support/Cursor/User/settings.json`
- Linux: `~/.config/Cursor/User/settings.json`

如果配置文件不存在，Claude 会自动创建。

### 问题：Cursor 中技能不生效

**检查清单：**
1. 配置文件是否为 `settings.json`（而非 `claude-code.json`）
2. 配置项是否为 `claude-code.skillsPath`（注意前缀）
3. Cursor 是否已重启
4. Cursor 设置中是否启用了 Claude Code

---

## 🎉 配置成功标志

### Claude Code CLI/桌面版

当配置成功后，你应该看到：

```
✅ 仓库已克隆：~/claude_skills
✅ 依赖安装完成
✅ 浏览器安装完成
✅ 配置文件已更新：~/.claude/settings.json
✅ skillsPath 已设置为：/path/to/claude_skills

配置完成！请重启 Claude Code 以加载技能。
```

### Cursor IDE

当配置成功后，你应该看到：

```
✅ 仓库已克隆：~/claude_skills
✅ 依赖安装完成
✅ 浏览器安装完成
✅ 配置文件已更新：~/Library/Application Support/Cursor/User/settings.json
✅ claude-code.skillsPath 已设置为：/path/to/claude_skills

配置完成！请重启 Cursor 以加载技能。
```

---

## 🚀 下一步

配置完成后：

1. **重启应用**（Claude Code 或 Cursor）
2. **验证安装**：询问 "What skills are available?"
3. **首次登录**：按照 README.md 中的说明登录小红书和 TikTok
4. **开始爬取**：享受自动化的社交媒体内容抓取！

---

## 📚 相关文档

- **完整说明**：查看 [README.md](README.md)
- **GitHub 仓库**：https://github.com/luoxikang/modulon-labs-tkskills
- **问题反馈**：https://github.com/luoxikang/modulon-labs-tkskills/issues

---

💡 **提示：** 将本文件收藏或打印，方便以后快速配置！

🎯 **快速选择：**
- 使用 Claude Code CLI/桌面版？→ 使用**第 1 个提示词**
- 使用 Cursor IDE？→ 使用**第 2 个提示词**
