# Odoo AI Ask DeepSeek 模块

[English](README.md)

## 概述

本模块扩展了 Odoo 19 企业版中的 AI 应用 (`ai_app`)，增加了对 DeepSeek AI 模型的支持。通过本模块，用户可以在 Odoo 的 "Ask AI" 功能中使用自己的 DeepSeek 账户进行交互。

## 功能特性

- **集成 DeepSeek 模型**: 在 Odoo 的 AI 代理中添加了 `deepseek-chat` 模型作为新的语言模型选项。
- **自定义 API 密钥**: 允许用户在 Odoo 设置中配置自己的 DeepSeek API 密钥，以便安全地连接到 DeepSeek 服务。
- **无缝体验**: 安装后，"Ask AI" 功能将自动获得使用 DeepSeek 的能力，无需复杂的额外设置。

## 安装

1.  将 `ai_app_deepseek` 文件夹复制到您的 Odoo `addons` 目录下。
2.  以开发者模式登录 Odoo。
3.  导航至 **应用** 菜单。
4.  点击 **更新应用列表**。
5.  搜索 `AI Ask DeepSeek` 模块并点击 **安装**。

## 配置

模块安装后，您需要配置 DeepSeek API 密钥才能使用该功能。

1.  导航至 **设置 -> 常规设置**。
2.  在 **AI** 部分，找到 **Use your own DeepSeek account** 选项。
3.  勾选该选项以启用自定义密钥。
4.  在下方的文本框中输入您的 DeepSeek API 密钥 (通常以 `sk-...` 开头)。
5.  点击 **保存**。

  <!-- 建议在此处替换为配置页面的截图链接 -->

## 使用方法

配置完成后，您可以在 Odoo 中任何集成了 "Ask AI" 功能的地方使用 DeepSeek 模型。

例如，在 Odoo 主界面的右上角，点击 "Ask AI" 图标，输入您的问题，系统将使用配置的 DeepSeek 模型来生成回答。

## 作者与支持

- **GitHub**: [https://github.com/cd-feng](https://github.com/cd-feng)

## 许可证

本模块基于 [AGPL-3](https://www.gnu.org/licenses/agpl-3.0.html) 许可证发布。
