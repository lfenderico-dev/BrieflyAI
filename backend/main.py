from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

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

@app.post("/summarization")
def AIsummarization(userKey:str, scrapedData:dict):
    # get scraped data
        title = scrapedData.get("Title", "")
        headings = scrapedData.get("Headings", [])
        paragraphs = scrapedData.get("Paragraphs", [])
        divs = scrapedData.get("Div", [])
        
        allContents = []
        
        if title:
            allContents.append(title)
        
        allContents.append(f"Title: {title}")
        allContents.append("Main headings: " + " ".join(headings))
        allContents.append("Content: " + " ".join(paragraphs, divs))
        
        content = " ".join(allContents)
        
        # gemini configuration
        genai.configure(api_key = userKey)
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        prompt = f"""
        Analyze this web content and create the most appropriate video summary.

        Instructions:
        1. Determine what type of content this is
        2. Structure your response to match that content type
        3. Make it engaging and suitable for video presentation
        4. Include visual suggestions relevant to the topic
        5. Keep it concise but comprehensive

        Always include:
        - An attention-grabbing title
        - The main message in simple terms  
        - 3-5 key points
        - How to make it visually interesting

        Content to analyze:
        {content}
        """
        
        # get the summary
        summary = model.generate_content(prompt)
        return {"summary": summary}
        