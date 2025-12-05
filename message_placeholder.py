from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful custoimer support agent'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt', 'r') as f:
    chat_history.extend(f.readlines())
print(chat_history)



# create out prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund?'})
print(prompt)  # For demonstration purposes

