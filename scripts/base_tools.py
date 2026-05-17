import os
from langchain.tools import tool
import ollama
import requests
import os 
from dotenv import load_dotenv
from langchain_tavily.tavily_search import TavilySearch

load_dotenv()


@tool
def get_seating_avalability(location:str,seating_availability:str):
    """Call to get the seating availability in a given location"""
    if location.lower()=='chennai' and seating_availability=='outdoor':
        return "Seats are available outdoor"
    elif location.lower()=='chennai' and seating_availability=='indoor':
        return "Seats are available indoor"
    else:
        return "Seats are not confirmed at given location please check after some time"
# -------------------------
# Weather Tool
# -------------------------

@tool
def get_weather(location: str):
    """Get current weather for a location using WeatherAPI.com.
    
    Use for queries about weather, temperature, or conditions in any city.
    Examples: "weather in Paris", "temperature in Tokyo", "is it raining in London"
    
    Args:
        location: City name (e.g., "New York", "London", "Tokyo")
        
    Returns:
        Current weather information including temperature and conditions.
    """

    if location.lower()=="chennai":
        return "38 deg celcius,Sunny"
    else:
        return "32 deg celcius,Clody"