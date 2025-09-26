from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()
API_KEY = os.getenv("API_KEY")

def scrapeUrl(url:str):
    webpage = requests.get(url, verify=False)
    scrapedWebpage = BeautifulSoup(webpage.content, "html.parser")
    
    headingsContent = [heading.get_text() for heading in scrapedWebpage.find_all(["h1", "h2"])]
    paragraphContent = [p.get_text() for p in scrapedWebpage.find_all("p")]
    divContent = [div.get_text() for div in scrapedWebpage.find_all("div")]
    
    main_section = [main.get_text() for main in scrapedWebpage.find_all("main")]
    section_section = [section.get_text() for section in scrapedWebpage.find_all("section")]
    article_section = [article.get_text() for article in scrapedWebpage.find_all("article")]
    
    title = scrapedWebpage.find("title").text

    def cleanContent(contentList):
        cleanedList = []
        for content in contentList:
            if len(content) > 10:
                cleanedList.append(content)
        return [' '.join(content.strip().split()) for content in cleanedList]
    
    clearedHeadingsContent = cleanContent(headingsContent)
    clearedParagraphContent = cleanContent(paragraphContent)
    clearedDivContent = cleanContent(divContent)
    clearedMainSection = cleanContent(main_section)
    clearedSectionSection = cleanContent(section_section)
    clearedArticleSection = cleanContent(article_section)
    
    
    
    result = "".join(clearedMainSection + clearedSectionSection + clearedArticleSection + clearedHeadingsContent + clearedParagraphContent + clearedDivContent)

    return {
        "content": result,
        "title": title
    }

def AIsummarization(content:str):
    prompt = f"""
    PROMPT:
    You are an expert content summarizer and information filter. Your task is to take the following scraped web content, identify only the most relevant and valuable information, and create a clear, comprehensive summary in plain text format.
    
    Requirements:
    - Use only plain text with no markdown formatting, special characters, or symbols
    - No hashtags, asterisks, bullets, or other formatting marks
    - Write in complete sentences and paragraphs
    - Summarize the key information in a logical, easy-to-follow structure
    - Explain complex concepts in simple terms
    - Keep the tone neutral and informative

    RELEVANCE FILTERING - INCLUDE ONLY:
    - Core subject matter and main themes
    - Factual information, data, and verified claims
    - Key insights, conclusions, and actionable takeaways
    - Important context that aids understanding
    - Significant developments, changes, or updates
    - Expert opinions and authoritative statements

    RELEVANCE FILTERING - EXCLUDE:
    - Advertisements, promotional content, and marketing fluff
    - Navigation elements, headers, footers, and website boilerplate
    - Repetitive information or redundant statements
    - Tangential topics that don't support the main subject
    - Personal anecdotes unless directly illustrative of key points
    - Technical metadata, timestamps, and formatting artifacts
    - Social media widgets, comments sections, and user-generated noise

    Your summary should include:
    - The main topic or subject matter
    - Key points and important details
    - Any significant data, findings, or conclusions
    - Context that helps readers understand the significance

    Content to summarize:{content}
    
    Instructions:
    First, scan the entire content to identify the core subject and filter out irrelevant material. Then provide a well-organized summary that captures only the essential, valuable information while making it accessible to a general audience. Focus on what truly matters to understanding the topic, discarding noise and filler content.
    """
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key= API_KEY,
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

@app.post("/summaryGeneration")
def generatesummary(url:dict):
    scrapedData = scrapeUrl(url["url"])
    summary = AIsummarization(scrapedData["content"])
    title = scrapedData["title"]
    return {"Summary": summary, "Title": title} 