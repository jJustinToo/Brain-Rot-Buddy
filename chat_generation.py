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
    "reddit": """Write a fictional Reddit story in the first person, based on the given topic. 
    The post should feel realistic, with specific details like ages, places, and personal experiences to make it believable. 
    Craft a strong, attention-grabbing title that reflects the essence of the story. 
    The story should be between 125-150 words, concise yet engaging, without unnecessary filler. 
    The tone should be casual, as if written by an everyday Reddit user sharing an interesting or bizarre experience. 
    Be sure to include emotional reactions, reflections, or thoughts to make the post relatable."
    Please do not use emojis.
    
    Topic: {topic}
    
    Output should look like this:
    <generated title, ending with puncuation sign.>
    <generated story that is 125-150words>
    
    """
}

def generate_text(type: str, topic: str):
    prompt = ChatPromptTemplate.from_template(templates[type])
    chain = prompt | model
    print(f'Generating a reddit story about "{topic}"...')
    result = chain.invoke({"topic": topic})
    print(colored(f'Text for a reddit story based on "{topic}" has been generated succesfully.', "green"))
    return markdown_to_plain_text(result).splitlines()