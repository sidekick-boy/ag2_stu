import os
from pathlib import Path

from dotenv import load_dotenv
from ag2.config import OpenAICompletionsConfig


# 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parents[1]
print("项目根目录：", PROJECT_ROOT)

# 加载 .env
load_dotenv(PROJECT_ROOT / ".env")

print("环境变量文件：", PROJECT_ROOT / ".env")

API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "未找到 DEEPSEEK_API_KEY，请检查项目根目录下的 .env 文件"
    )


def get_llm_config():
    """创建 DeepSeek 模型配置"""

    return OpenAICompletionsConfig(
        model="deepseek-flash",
        api_key=API_KEY,
        base_url="https://api.deepseek.com",
    )