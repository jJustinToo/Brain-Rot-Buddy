from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.1")
def generateRedditStory(topic):
    print("Generating text...")
    template = """
    Create a story based on the topic below

    Please limit the story to 125 words but also generate atleast 100 words. This is a hard rule.
    
    Topic: {topic}

    Story: 
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model  

    result = chain.invoke({"topic": topic})
    print(f'Text for a reddit story based on "{topic}" has been generated succesfully.')
    return result

def produceImages(topic):
    print("Generating text...")
    template = """
    Create a story based on the topic below

    Please limit the story to 125 words but also generate atleast 100 words. This is a hard rule.
    
    Topic: {topic}

    Story: 
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model  

    result = chain.invoke({"topic": topic})
    print(f'Text for a reddit story based on "{topic}" has been generated succesfully.')
    return result