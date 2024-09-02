from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from termcolor import colored
import markdown
from bs4 import BeautifulSoup


def markdown_to_plain_text(markdown_text):
    # Convert Markdown to HTML
    html = markdown.markdown(markdown_text)
    # Use BeautifulSoup to extract plain text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()


# model = OllamaLLM(model="llama3.1")
model = OllamaLLM(model="gemma2:2b")

templates = {
    "redditStory": """Write a Reddit-style story in the first person, starting with a catchy and dramatic title that captures attention. The title should mimic the style of popular Reddit posts, be between 15-20 words long, and include specific details such as age and gender (e.g., "I (33 MALE) am divorcing my wife (33 FEMALE) after discovering the truth."). Adjust the ages to fit the narrative.

    The story should follow the format and tone of posts commonly found in subreddits like r/relationships or r/AmItheAsshole, where the narrator describes a personal experience. The content should be engaging, believable, and evoke strong emotions, but it must remain plausible. The story should be 100-125 words long with no filler, focusing on making the narrative vivid, relatable, and memorable.
    **Important:** Do not repeat or reuse the provided example titles or content. Create an original title and story based on the specific topic provided. 100-125 words is a hard rule. I will not accept a story with words less than or over
    Please only use text and proper grammer. 
    Please note that all text generated will be text to speeched later.
    
    Topic: {topic}

    **Formatting Notes:**
    * Use plain text only. Do not include any symbols, hashtags, or other formatting characters in the title or content.
    * All acronyms should be written out as words as best as you can.
    * When generating a title, write it out as plain text only. Avoid using any extraneous symbols or formatting.
    * The title and content should only contain regular text, without any special characters or formatting.
    * The generated text will be used for text-to-speech processing, so ensure it is clean and free from any non-text symbols.
    * Please also write with proper punctuation like commas and full stops and quotes to emphasise speech patterns.

    Please format the output as follows:
    <Your generated title>
    <Your generated content>"""
}


redditPrompt = ChatPromptTemplate.from_template(templates["redditStory"])
redditChain = redditPrompt | model  

def generateRedditStory(topic: str):
    print(f'Generating a reddit story about "{topic}"...')
    result = redditChain.invoke({"topic": topic})
    print(colored(f'Text for a reddit story based on "{topic}" has been generated succesfully.', "green"))
    return markdown_to_plain_text(result)


# def generateWYR():

def produceImages(topic):
    pass

