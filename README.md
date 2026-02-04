# 🛠️ Cicy Utils

**[English](#english) | [中文](#中文)**

Cross-platform development utilities and tools that work everywhere.

---

## English

### 🚀 Quick Start

#### Installation
```bash
pip install cicy-utils
```

#### Usage
```bash
# Basic hello world
cicy hello

# Hello with custom name
cicy hello --name "Developer"

# Different output styles
cicy hello --style simple
cicy hello --style info
cicy hello --style fancy

# Show version and check for updates
cicy version

# Update to latest version
cicy update
```

### ✨ Features

- **Cross-platform**: Works on Windows, macOS, and Linux
- **Rich output**: Beautiful terminal output with colors and formatting
- **Extensible**: Easy to add new utilities and tools
- **Developer-friendly**: Built for developers, by developers

### 🎯 What This Does

The `hello` command demonstrates:
- System information detection
- Cross-platform compatibility
- Rich terminal output
- Multiple output styles
- Command-line argument handling

### 📋 Commands

- `cicy hello` - Interactive hello world with system info
- `cicy version` - Show version information and check for updates
- `cicy update` - Update to the latest version from PyPI
- `cicy --help` - Show all available commands

### 🔧 Development

```bash
# Clone repository
git clone https://github.com/cicy-dev/cicy-utils.git
cd cicy-utils

# Install in development mode
pip install -e .

# Run tests
pytest

# Format code
black cicy_utils/
```

---

## 中文

### 🚀 快速开始

#### 安装
```bash
pip install cicy-utils
```

#### 使用
```bash
# 基本的 hello world
cicy hello

# 自定义名称的问候
cicy hello --name "开发者"

# 不同的输出样式
cicy hello --style simple
cicy hello --style info
cicy hello --style fancy

# 显示版本并检查更新
cicy version

# 更新到最新版本
cicy update
```

### ✨ 特性

- **跨平台**: 支持 Windows、macOS 和 Linux
- **丰富输出**: 美观的终端输出，支持颜色和格式化
- **可扩展**: 易于添加新的实用工具
- **开发者友好**: 为开发者而生

### 🎯 功能说明

`hello` 命令演示了:
- 系统信息检测
- 跨平台兼容性
- 丰富的终端输出
- 多种输出样式
- 命令行参数处理

### 📋 命令

- `cicy hello` - 交互式 hello world 和系统信息
- `cicy version` - 显示版本信息并检查更新
- `cicy update` - 从 PyPI 更新到最新版本
- `cicy --help` - 显示所有可用命令

### 🔧 开发

```bash
# 克隆仓库
git clone https://github.com/cicy-dev/cicy-utils.git
cd cicy-utils

# 开发模式安装
pip install -e .

# 运行测试
pytest

# 格式化代码
black cicy_utils/
```
