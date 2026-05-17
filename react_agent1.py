from langchain_ollama.chat_models import ChatOllama
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from scripts.base_tools import get_weather,get_seating_avalability
from langchain_tavily import TavilySearch

if __name__=="__main__":
    load_dotenv()
    llm=ChatOllama(model="qwen3:30b",temperature=0)
    tavily_search=TavilySearch(max_results=2)
    tools=[get_weather,get_seating_avalability,tavily_search]
    system_prompt="""You are a financial analyst in analyzing tech stocks\n Provide data driven analysys with clear insights.you have access to web_search tool and get_weather tool"""
    agent=create_agent(model=llm,tools=tools,system_prompt=system_prompt)
    response=agent.invoke({"messages":[HumanMessage(content="What is the Current Weather in Chennai")]})
    print(response['messages'][-1].content)