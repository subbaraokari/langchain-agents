from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

if __name__=="__main__":
    load_dotenv()
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    response=llm.invoke("Tell me a joke about monkey")
    print(response.content)