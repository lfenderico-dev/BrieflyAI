from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/scraper")
def scrapeUrl(url:str):
    webpage = requests.get(url)
    scrapedWebpage = BeautifulSoup(webpage.content, "html.parser")
    
    title = scrapedWebpage.find("title").text
    headingsContent = [heading.get_text() for heading in scrapedWebpage.find_all(["h1", "h2"])]
    paragraphContent = [p.get_text() for p in scrapedWebpage.find_all("p")]
    divContent = [div.get_text() for div in scrapedWebpage.find_all("div")]

    def cleanContent(contentList):
        cleanedList = []
        for content in contentList:
            if len(content) > 10:
                cleanedList.append(content)
        return [' '.join(content.strip().split()) for content in cleanedList]
    
    clearedHeadingsContent = cleanContent(headingsContent)
    clearedParagraphContent = cleanContent(paragraphContent)
    clearedDivContent = cleanContent(divContent)

    result = {
        "Title": title,
        "Headings": clearedHeadingsContent,
        "Paragraphs": clearedParagraphContent,
        "Div": clearedDivContent
    }

    return result