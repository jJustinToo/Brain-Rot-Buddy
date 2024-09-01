from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from termcolor import colored

# model = OllamaLLM(model="llama3.1")
model = OllamaLLM(model="gemma2:2b")

templates = {
    "redditStory": """Create a story based on the topic below\n\nPlease limit the story to 125 words but also generate atleast 100 words. This is a hard rule. Please refrain from writing any filler from your reply like "This is a good prompt". Please only return the story's text. I do not want any other information such as the word count.\n\nTopic: {topic}\n\nStory: """
}
redditPrompt = ChatPromptTemplate.from_template(templates["redditStory"])
redditChain = redditPrompt | model  

def generateRedditStory(topic: str):
    print(f'Generating a reddit story about "{topic}"...')
    result = redditChain.invoke({"topic": topic})
    print(colored(f'Text for a reddit story based on "{topic}" has been generated succesfully.', "green"))
    return result

def produceImages(topic):
    pass