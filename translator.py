from typing import Any
import os
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("translator")

# Constants
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

async def make_deepseek_request(question: str) -> dict[str, Any] | None:
    """Make a request to the DeepSeek API with proper error handling."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful translation assistant. Please translate the following text."},
            {"role": "user", "content": question}
        ],
        "stream": False
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                DEEPSEEK_API_URL, 
                headers=headers, 
                json=data,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error making DeepSeek API request: {str(e)}")
            return None

@mcp.tool()
async def translate(text: str) -> str:
    """Translate text using DeepSeek API.

    Args:
        text: The text to translate
    """
    if not DEEPSEEK_API_KEY:
        return "Error: DeepSeek API key not found in environment variables."

    response_data = await make_deepseek_request(text)
    
    if not response_data:
        return "Error: Unable to get translation from DeepSeek API."
        
    try:
        translated_text = response_data["choices"][0]["message"]["content"]
        return translated_text
    except (KeyError, IndexError) as e:
        print(f"Error extracting translation from response: {str(e)}")
        return "Error: Unable to extract translation from API response."

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') 