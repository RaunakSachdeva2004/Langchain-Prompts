from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# 1. Setup the Model
# We use the exact name of the model you downloaded: "deepseek-r1:7b"
llm = ChatOllama(
    model="deepseek-r1:7b", 
    temperature=0.6,  # Reasoning models work best with lower temperature (0.5 - 0.7)
)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant.')
]

print("✅ DeepSeek R1 (7B) is ready! Type 'exit' to quit.")
print("-" * 50)

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    
    chat_history.append(HumanMessage(content=user_input))
    
    try:
        print("Thinking...", end="\r") # Visual indicator
        result = llm.invoke(chat_history)
        
        chat_history.append(result)
        
        print("AI: ", result.content)
        print("-" * 50)
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the Ollama app is running in the background!")