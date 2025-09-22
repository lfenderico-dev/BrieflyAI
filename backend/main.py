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

def generateVideo(summary:str):
    client = Client("Lightricks/ltx-video-distilled")
    AIVideo = client.predict(
		prompt=f"Generate a video from this content: {summary}",
		negative_prompt="worst quality, inconsistent motion, blurry, jittery, distorted",
		input_image_filepath=None,
		input_video_filepath=None,
		height_ui=512,
		width_ui=704,
		mode="image-to-video",
		duration_ui=120,
		ui_frames_to_use=9,
		seed_ui=42,
		randomize_seed=True,
		ui_guidance_scale=1,
		improve_texture_flag=True,
		api_name="/text_to_video"
    )
    return AIVideo


@app.post("/VideoGeneration")
def generateVideo(userKey:str, url:str):
    scrapedData = scrapeUrl(url)
    summary = AIsummarization(userKey, scrapedData)
    AIVideo = generateVideo(summary)
    
    return{
        "Summary": summary,
        "Video": AIVideo
    }