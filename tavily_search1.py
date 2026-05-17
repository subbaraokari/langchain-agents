from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

search=TavilySearch(max_results=2)
results=search.invoke("What is the current stock price of apple")
print(results)