
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient
from rich import print

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def web_search(query: str) -> str:
    """Search the web for information about a research topic."""
    results = tavily.search(query=query, max_results=5)

    output = []
    for result in results.get("results", []):
        output.append(
            f"Title: {result.get('title')}\n"
            f"URL: {result.get('url')}\n"
            f"Content: {result.get('content')}"
        )

    return "\n\n".join(output)


@tool
def scrape_url(url: str) -> str:
    """Extract readable text content from a webpage."""
    try:
        response = requests.get(
            url,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        text = soup.get_text(separator=" ", strip=True)
        return text[:12000]

    except requests.RequestException as e:
        return f"Error scraping URL: {str(e)}"
