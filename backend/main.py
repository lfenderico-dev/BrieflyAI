from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/scraper")
def scrapeUrl(url:str):
    webpage = requests.get(url)
    scrapedWebpage = BeautifulSoup(webpage.content, "html.parser")
    
    title = scrapedWebpage.find("title").text
    headingsContent = [heading.get_text() for heading in scrapedWebpage.find_all("h1", "h2")]
    paragraphContent = [p.get_text() for p in scrapedWebpage.find_all("p")]

    result = {
        "Title": title,
        "Headings": headingsContent,
        "Paragraphs": paragraphContent
    }

    return result