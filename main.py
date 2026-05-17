from langchain_ollama import ChatOllama
from dotenv import load_dotenv

if __name__=="__main__":
    load_dotenv()
    llm=ChatOllama(model="qwen3:30b",temperature=0.7)
    response=llm.invoke("Tell me joke about Ollama?")
    response.pretty_print()
