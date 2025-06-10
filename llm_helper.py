from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
llm = ChatGroq(
    groq_api_key = os.getenv("GROQ_API_KEY"),
    model_name ="gemma2-9b-it"
)


if __name__== "__main__":
    response = llm.invoke("give me ingredients of momos with emojis")
    print(response.content)