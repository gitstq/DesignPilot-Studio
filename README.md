<div align="center">

# 🎨 DesignPilot Studio

**Lightweight AI Design System Extraction & Visualization Engine**
**轻量级AI设计系统提取与可视化引擎**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)]()
[![10 Presets](https://img.shields.io/badge/Presets-10_Chinese_Products-orange.svg)]()
[![5 Export Formats](https://img.shields.io/badge/Exports-CSS%20%7C%20JSON%20%7C%20Tailwind%20%7C%20SCSS%20%7C%20LESS-purple.svg)]()

[English](#english) · [简体中文](#简体中文) · [繁體中文](#繁體中文)

<p>
<img src="https://img.shields.io/badge/微信-WeChat-07C160?style=flat-square" alt="WeChat">
<img src="https://img.shields.io/badge/支付宝-Alipay-1677FF?style=flat-square" alt="Alipay">
<img src="https://img.shields.io/badge/飞书-Feishu-3370FF?style=flat-square" alt="Feishu">
<img src="https://img.shields.io/badge/小红书-Xiaohongshu-FF2442?style=flat-square" alt="Xiaohongshu">
<img src="https://img.shields.io/badge/钉钉-DingTalk-2F83FA?style=flat-square" alt="DingTalk">
<img src="https://img.shields.io/badge/B站-Bilibili-00A1D6?style=flat-square" alt="Bilibili">
<img src="https://img.shields.io/badge/淘宝-Taobao-FF5000?style=flat-square" alt="Taobao">
<img src="https://img.shields.io/badge/抖音-Douyin-FE2C55?style=flat-square" alt="Douyin">
<img src="https://img.shields.io/badge/美团-Meituan-FFC300?style=flat-square" alt="Meituan">
<img src="https://img.shields.io/badge/通用-Modern-6366F1?style=flat-square" alt="Modern">
</p>

</div>

---

## 简体中文

### 🎉 项目介绍

**DesignPilot Studio** 是一款轻量级AI设计系统提取与可视化引擎，灵感来源于GitHub上4天突破2万Star的 [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) 项目。

**核心痛点**：在AI编程时代（Vibe Coding），AI生成的UI往往缺乏设计一致性。DesignPilot Studio 通过结构化的设计令牌（Design Tokens）和可视化预览，让AI能够理解并复现像素级一致的用户界面。

**差异化亮点**：
- 🇨🇳 **专注中国产品**：内置10个中国顶级产品的设计系统预设（微信、支付宝、飞书等）
- 🔧 **CLI工具链**：不仅是静态文档，更是完整的命令行工具
- 📦 **零外部依赖**：纯Python 3.8+标准库实现，无需安装任何第三方包
- 🎨 **多格式导出**：支持CSS、JSON、Tailwind、SCSS、LESS五种格式
- 🤖 **AI友好**：生成的DESIGN.md可直接提供给AI编码工具使用

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🎨 **10个内置预设** | 微信、支付宝、飞书、小红书、钉钉、B站、淘宝、抖音、美团、通用现代 |
| 🔍 **CSS令牌提取** | 自动从CSS/HTML文件中提取颜色、字体、间距、阴影等设计令牌 |
| 📄 **DESIGN.md生成** | 生成结构化的设计系统文档（支持中英文） |
| 🖼️ **交互式预览** | 生成自包含的HTML预览文件，可直接在浏览器中查看 |
| 📦 **5种导出格式** | CSS自定义属性、JSON、Tailwind配置、SCSS变量、LESS变量 |
| ✅ **设计系统验证** | 自动检测设计系统的一致性和完整性，给出评分 |
| 🚀 **项目初始化** | 一键生成完整的设计系统项目结构 |
| 🌐 **零外部依赖** | 纯Python标准库实现，跨平台兼容 |

### 🚀 快速开始

**环境要求**：Python 3.8+（无需安装任何第三方依赖）

```bash
# 克隆仓库
git clone https://github.com/gitstq/DesignPilot-Studio.git
cd DesignPilot-Studio

# 查看帮助
python -m src.cli --help

# 初始化一个新项目（使用微信设计系统）
python -m src.cli init --name my-app --preset wechat

# 查看所有可用预设
python -m src.cli list

# 生成DESIGN.md
python -m src.cli generate --preset alipay --lang zh

# 生成交互式HTML预览
python -m src.cli preview --preset feishu

# 导出为多种格式
python -m src.cli export --preset xiaohongshu --formats css json tailwind scss less

# 从CSS文件提取设计令牌
python -m src.cli extract --source styles.css --output tokens.json

# 验证设计系统
python -m src.cli validate --input DESIGN.md
```

### 📖 详细使用指南

#### 1️⃣ 初始化项目

```bash
# 使用预设快速初始化
python -m src.cli init --name my-design-system --preset wechat

# 生成的项目结构：
# my-design-system/
# ├── DESIGN.md          # 中文设计系统文档
# ├── DESIGN.en.md       # 英文设计系统文档
# ├── preview/
# │   └── index.html     # 交互式预览
# ├── tokens/
# │   └── design-tokens.json  # 令牌数据
# ├── src/
# │   ├── design-tokens.css   # CSS自定义属性
# │   ├── tailwind.config.js  # Tailwind配置
# │   └── design-tokens.scss  # SCSS变量
# ├── .gitignore
# └── package.json
```

#### 2️⃣ 应用预设到现有项目

```bash
# 生成支付宝设计系统的DESIGN.md和预览
python -m src.cli apply alipay --output ./design

# 生成飞书设计系统的CSS变量
python -m src.cli apply feishu --output ./design --formats css json
```

#### 3️⃣ 从现有CSS提取设计令牌

```bash
# 从CSS文件提取
python -m src.cli extract --source path/to/styles.css --output tokens.json

# 从HTML文件提取
python -m src.cli extract --source path/to/page.html --output tokens.json --format html
```

#### 4️⃣ 与AI编码工具配合使用

```bash
# 步骤1：生成DESIGN.md
python -m src.cli generate --preset wechat --lang zh

# 步骤2：将DESIGN.md提供给AI编码工具（Claude Code、Cursor等）
# 步骤3：AI会按照设计系统规范生成一致的UI组件
```

### 💡 设计思路与迭代规划

**设计理念**：
- 将设计系统降维为结构化文档，让AI可以直接理解
- 每个预设都包含AI提示词，可直接复制使用
- 零依赖设计，确保在任何Python环境下都能运行

**后续迭代计划**：
- [ ] 支持从Figma文件提取设计令牌
- [ ] 增加更多中国产品预设（QQ、网易云音乐、知乎等）
- [ ] 支持暗色模式令牌自动生成
- [ ] 添加Web UI界面
- [ ] 支持设计令牌的diff和版本对比

### 📦 打包与部署

本项目为纯Python CLI工具，无需打包部署：

```bash
# 直接运行
python -m src.cli <command>

# 或添加到PATH后直接使用
export PATH="/path/to/DesignPilot-Studio:$PATH"
designpilot <command>
```

### 🤝 贡献指南

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 发起 Pull Request

### 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

## 繁體中文

### 🎉 專案介紹

**DesignPilot Studio** 是一款輕量級AI設計系統提取與視覺化引擎，靈感來源於GitHub上4天突破2萬Star的 [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) 專案。

**核心痛點**：在AI程式設計時代（Vibe Coding），AI生成的UI往往缺乏設計一致性。DesignPilot Studio 透過結構化的設計令牌（Design Tokens）和視覺化預覽，讓AI能夠理解並重現像素級一致的使用者介面。

**差異化亮點**：
- 🇨🇳 **專注中國產品**：內建10個中國頂級產品的設計系統預設（微信、支付寶、飛書等）
- 🔧 **CLI工具鏈**：不僅是靜態文檔，更是完整的命令列工具
- 📦 **零外部依賴**：純Python 3.8+標準庫實現，無需安裝任何第三方套件
- 🎨 **多格式匯出**：支援CSS、JSON、Tailwind、SCSS、LESS五種格式
- 🤖 **AI友善**：生成的DESIGN.md可直接提供給AI編碼工具使用

### ✨ 核心特性

| 特性 | 說明 |
|------|------|
| 🎨 **10個內建預設** | 微信、支付寶、飛書、小紅書、釘釘、B站、淘寶、抖音、美團、通用現代 |
| 🔍 **CSS令牌提取** | 自動從CSS/HTML檔案中提取顏色、字體、間距、陰影等設計令牌 |
| 📄 **DESIGN.md生成** | 生成結構化的設計系統文檔（支援中英文） |
| 🖼️ **互動式預覽** | 生成自包含的HTML預覽檔案，可直接在瀏覽器中查看 |
| 📦 **5種匯出格式** | CSS自訂屬性、JSON、Tailwind配置、SCSS變數、LESS變數 |
| ✅ **設計系統驗證** | 自動檢測設計系統的一致性和完整性，給出評分 |
| 🚀 **專案初始化** | 一鍵生成完整的設計系統專案結構 |
| 🌐 **零外部依賴** | 純Python標準庫實現，跨平台相容 |

### 🚀 快速開始

**環境要求**：Python 3.8+（無需安裝任何第三方依賴）

```bash
# 克隆倉庫
git clone https://github.com/gitstq/DesignPilot-Studio.git
cd DesignPilot-Studio

# 查看幫助
python -m src.cli --help

# 初始化一個新專案（使用微信設計系統）
python -m src.cli init --name my-app --preset wechat

# 查看所有可用預設
python -m src.cli list

# 生成DESIGN.md
python -m src.cli generate --preset alipay --lang zh

# 生成互動式HTML預覽
python -m src.cli preview --preset feishu

# 匯出為多種格式
python -m src.cli export --preset xiaohongshu --formats css json tailwind scss less

# 從CSS檔案提取設計令牌
python -m src.cli extract --source styles.css --output tokens.json

# 驗證設計系統
python -m src.cli validate --input DESIGN.md
```

### 📖 詳細使用指南

#### 1️⃣ 初始化專案

```bash
# 使用預設快速初始化
python -m src.cli init --name my-design-system --preset wechat

# 生成的專案結構：
# my-design-system/
# ├── DESIGN.md          # 中文設計系統文檔
# ├── DESIGN.en.md       # 英文設計系統文檔
# ├── preview/
# │   └── index.html     # 互動式預覽
# ├── tokens/
# │   └── design-tokens.json  # 令牌資料
# ├── src/
# │   ├── design-tokens.css   # CSS自訂屬性
# │   ├── tailwind.config.js  # Tailwind配置
# │   └── design-tokens.scss  # SCSS變數
# ├── .gitignore
# └── package.json
```

#### 2️⃣ 與AI編碼工具配合使用

```bash
# 步驟1：生成DESIGN.md
python -m src.cli generate --preset wechat --lang zh

# 步驟2：將DESIGN.md提供給AI編碼工具（Claude Code、Cursor等）
# 步驟3：AI會按照設計系統規範生成一致的UI組件
```

### 💡 設計思路與迭代規劃

**設計理念**：
- 將設計系統降維為結構化文檔，讓AI可以直接理解
- 每個預設都包含AI提示詞，可直接複製使用
- 零依賴設計，確保在任何Python環境下都能運行

**後續迭代計劃**：
- [ ] 支援從Figma檔案提取設計令牌
- [ ] 增加更多中國產品預設（QQ、網易雲音樂、知乎等）
- [ ] 支援暗色模式令牌自動生成
- [ ] 添加Web UI介面
- [ ] 支援設計令牌的diff和版本對比

### 🤝 貢獻指南

歡迎貢獻！請閱讀 [CONTRIBUTING.md](CONTRIBUTING.md) 了解詳情。

### 📄 開源協議

本專案基於 [MIT License](LICENSE) 開源。

---

## English

### 🎉 Introduction

**DesignPilot Studio** is a lightweight AI design system extraction and visualization engine, inspired by [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) which gained 20,000+ stars in just 4 days on GitHub.

**The Problem**: In the AI coding era (Vibe Coding), AI-generated UIs often lack design consistency. DesignPilot Studio solves this by providing structured design tokens and visual previews that AI coding tools can directly understand and reproduce.

**Key Differentiators**:
- 🇨🇳 **China-Focused Presets**: 10 built-in design systems from top Chinese products (WeChat, Alipay, Feishu, etc.)
- 🔧 **Full CLI Toolkit**: Not just static docs — a complete command-line toolchain
- 📦 **Zero Dependencies**: Pure Python 3.8+ standard library, no third-party packages needed
- 🎨 **Multi-Format Export**: CSS, JSON, Tailwind, SCSS, LESS
- 🤖 **AI-Friendly**: Generated DESIGN.md files can be directly fed to AI coding tools

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🎨 **10 Built-in Presets** | WeChat, Alipay, Feishu, Xiaohongshu, DingTalk, Bilibili, Taobao, Douyin, Meituan, Modern |
| 🔍 **CSS Token Extraction** | Auto-extract colors, typography, spacing, shadows from CSS/HTML files |
| 📄 **DESIGN.md Generation** | Generate structured design system docs (Chinese & English) |
| 🖼️ **Interactive Preview** | Self-contained HTML preview, viewable in any browser |
| 📦 **5 Export Formats** | CSS custom properties, JSON, Tailwind config, SCSS variables, LESS variables |
| ✅ **Design Validation** | Auto-check consistency and completeness with scoring |
| 🚀 **Project Init** | One-command project scaffolding with full structure |
| 🌐 **Zero Dependencies** | Pure Python standard library, cross-platform |

### 🚀 Quick Start

**Requirements**: Python 3.8+ (no third-party dependencies needed)

```bash
# Clone the repository
git clone https://github.com/gitstq/DesignPilot-Studio.git
cd DesignPilot-Studio

# View help
python -m src.cli --help

# Initialize a new project with WeChat design system
python -m src.cli init --name my-app --preset wechat

# List all available presets
python -m src.cli list

# Generate DESIGN.md
python -m src.cli generate --preset alipay --lang en

# Generate interactive HTML preview
python -m src.cli preview --preset feishu

# Export to multiple formats
python -m src.cli export --preset xiaohongshu --formats css json tailwind scss less

# Extract design tokens from CSS
python -m src.cli extract --source styles.css --output tokens.json

# Validate design system
python -m src.cli validate --input DESIGN.md
```

### 📖 Detailed Usage Guide

#### 1️⃣ Initialize a Project

```bash
# Quick init with a preset
python -m src.cli init --name my-design-system --preset wechat

# Generated project structure:
# my-design-system/
# ├── DESIGN.md          # Chinese design system doc
# ├── DESIGN.en.md       # English design system doc
# ├── preview/
# │   └── index.html     # Interactive preview
# ├── tokens/
# │   └── design-tokens.json  # Token data
# ├── src/
# │   ├── design-tokens.css   # CSS custom properties
# │   ├── tailwind.config.js  # Tailwind config
# │   └── design-tokens.scss  # SCSS variables
# ├── .gitignore
# └── package.json
```

#### 2️⃣ Use with AI Coding Tools

```bash
# Step 1: Generate DESIGN.md
python -m src.cli generate --preset wechat --lang en

# Step 2: Feed DESIGN.md to your AI coding tool (Claude Code, Cursor, etc.)
# Step 3: AI will generate pixel-perfect UI components following the design system
```

#### 3️⃣ Extract from Existing CSS

```bash
# Extract from CSS file
python -m src.cli extract --source path/to/styles.css --output tokens.json

# Extract from HTML file
python -m src.cli extract --source path/to/page.html --output tokens.json --format html
```

### 💡 Design Philosophy & Roadmap

**Design Philosophy**:
- Reduce design systems to structured documents that AI can directly understand
- Each preset includes an AI prompt that can be copied and used directly
- Zero-dependency design ensures it runs in any Python environment

**Roadmap**:
- [ ] Figma file design token extraction
- [ ] More Chinese product presets (QQ, NetEase Cloud Music, Zhihu, etc.)
- [ ] Dark mode token auto-generation
- [ ] Web UI interface
- [ ] Design token diff and version comparison

### 📦 Packaging & Deployment

This is a pure Python CLI tool — no packaging needed:

```bash
# Run directly
python -m src.cli <command>

# Or add to PATH
export PATH="/path/to/DesignPilot-Studio:$PATH"
designpilot <command>
```

### 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Made with ❤️ by DesignPilot Team**

*Zero Dependencies · Pure Python · AI-First Design*

</div>
