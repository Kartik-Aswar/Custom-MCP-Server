# import requests
import os
from dotenv import load_dotenv
load_dotenv()
city = "London"
api_key = os.getenv("WEATHER_API_KEY")
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

import httpx

async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no")
        if response.status_code == 200:
            data = response.json()
            print(f"Current weather in {city}:")
            print(f"Temperature: {data['current']['temp_c']}°C")
            print(f"Weather: {data['current']['condition']['text']}")
            print(f"Humidity: {data['current']['humidity']}%")
            print(f"Wind: {data['current']['wind_kph']} km/h")
            print(f"Feels like: {data['current']['feelslike_c']}°C")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    


if __name__ == "__main__":
    import asyncio
    
    async def main():
        weather_data = await fetch_weather("Pune")
        print(weather_data)
    
    asyncio.run(main())

