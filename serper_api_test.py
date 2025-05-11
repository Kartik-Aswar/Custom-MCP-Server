import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
# Your serper API key
api_key = os.getenv("SERPER_API_KEY")



import httpx

async def serper_search_results(query: str) -> str:
    """Fetch search results from Serper API (Google Search)"""
    headers = {
        "X-API-KEY": api_key,  # Serper uses X-API-KEY header
        "Content-Type": "application/json"
    }

    params = {
        "q": query,          # Search query
        "num": 10,            # Number of results (Serper uses 'num' instead of 'count')
        "tbs": "qdr:w"        # Time filter: 'qdr:w' = past week
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://google.serper.dev/search",
            headers=headers,
            params=params
        )
        return response.json()  # Serper returns JSON by default

if __name__ == "__main__":
    import asyncio
    
    async def main():
        search_data = await serper_search_results("Bengal Riots in April 2025")
        print(search_data)
    
    asyncio.run(main())