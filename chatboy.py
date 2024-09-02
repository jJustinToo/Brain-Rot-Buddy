from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# model = OllamaLLM(model="llama3.1")
model = OllamaLLM(model="gemma2:2b")

# act like you are having a conversation. Not a QNA
# Please emphasise speed over accuracy. I want the fastest response possible. Limit the word count.

template = """You are a chatbot,
Answer the question below:

Here is the conversation history: {context}

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model  


def handle_convo():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", 'quit', 'bye']:
            break
        result = chain.invoke({"context": context, "question": user_input})
        print(f"Bot: {result}".strip("\n"))
        context += f"\nUser: {user_input}\Bot: {result}"
        
handle_convo()