from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

app = FastAPI()

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

    result = "".join(clearedHeadingsContent + clearedParagraphContent + clearedDivContent)

    return result

def AIsummarization(userKey:str, content:str):
    prompt = f"""
    Summarize the following content: {content}
    """
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key= userKey,
    )

    completion = client.chat.completions.create(
        model="x-ai/grok-4-fast:free",
        messages=[
            {
            "role": "user",
            "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content

@app.post("/VideoGeneration")
def generateVideo(userKey:str, url:str):
    scrapedData = scrapeUrl(url)
    summary = AIsummarization(userKey, scrapedData)
    return {"Summary": summary}