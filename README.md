# MCP Translation Server
# MCP 翻译服务器

This MCP server provides translation capabilities using the DeepSeek API.
# 这个 MCP 服务器使用 DeepSeek API 提供翻译功能。

## Setup
## 设置

1. Install Python 3.10 or higher
# 1. 安装 Python 3.10 或更高版本

2. Install dependencies:
# 2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. Set up environment variables:
# 3. 设置环境变量：

Create a `.env` file in the project root with your DeepSeek API key:
# 在项目根目录创建一个 `.env` 文件，包含你的 DeepSeek API 密钥：

```
DEEPSEEK_API_KEY=your_api_key_here
```

## Running the Server
## 运行服务器

Run the server using:
# 使用以下命令运行服务器：

```bash
python translator.py
```

## 作为MCP服务器工具
## 在MCP客户端（如Claude Desktop、Cursor等）中配置此服务：
    "m-c-p": {
      "command": "python",
      "args": [
        "你的路径\\translator.py"
      ],
      "env":{
        "DEEPSEEK_API_KEY":"你的Api Key"
      }
    }

### translate
### 翻译

Translates text using the DeepSeek API.
# 使用 DeepSeek API 翻译文本。

Parameters:
# 参数：
- `text` (string): The text to translate
# - `text` (字符串)：要翻译的文本

Returns:
# 返回：
- A string containing the translated text
# - 包含翻译后文本的字符串

## Error Handling
## 错误处理

The server handles various error cases:
# 服务器处理各种错误情况：

- Missing API key
# - API 密钥缺失
- API request failures
# - API 请求失败
- Invalid API responses
# - 无效的 API 响应

Each error case returns a descriptive error message. 
# 每种错误情况都会返回描述性的错误消息。 