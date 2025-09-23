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
    Please analyze the following scraped web content and create a comprehensive summary following these guidelines:

    **CONTENT PROCESSING:**
    1. Clean and format the raw text by:
    - Removing excessive whitespace, line breaks (\n), and formatting artifacts
    - Eliminating navigation menus, footer content, ads, and boilerplate text
    - Filtering out repetitive elements and spam content
    - Preserving only the core informational content

    **SUMMARIZATION REQUIREMENTS:**
    2. Create a structured summary that includes:
    - **Main Topic**: A clear statement of what the content is about
    - **Key Points**: 3-5 most important insights or findings (use bullet points)
    - **Supporting Details**: Relevant context, data, or examples that add value
    - **Conclusion/Takeaway**: The primary message or actionable insight

    **QUALITY STANDARDS:**
    3. Ensure your summary is:
    - **Concise**: Reduce original content by 70-80% while retaining essential information
    - **Coherent**: Use clear, professional language with smooth transitions
    - **Accurate**: Stay faithful to the original meaning and facts
    - **Objective**: Present information neutrally without adding personal opinions
    - **Actionable**: Highlight practical insights or implications when present

    **FORMAT:**
    4. Present the final summary in clean, readable plain text format with:
    - Proper paragraph structure
    - Clear section headings
    - Bullet points for lists
    - No unnecessary formatting characters or symbols

    **CONTENT TO ANALYZE:**
    {content}

    Please provide only the cleaned and summarized content without any meta-commentary about the process.
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

@app.post("/summaryGeneration")
def generatesummary(userKey:str, url:str):
    scrapedData = scrapeUrl(url)
    summary = AIsummarization(userKey, scrapedData)
    return {"Summary": summary}