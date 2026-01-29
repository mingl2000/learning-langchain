from langchain_openai.chat_models import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# the building blocks

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)

model = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat" 
)

# combine them with the | operator

chatbot = template | model

# use it

response = chatbot.invoke({"question": "Which model providers offer LLMs?"})
print(response.content)

# streaming

for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)
