from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("TOGETHER_API_KEY"),
    openai_api_base="https://api.together.xyz/v1",
    model_name="mistralai/Mixtral-8x7B-Instruct-v0.1"
)
