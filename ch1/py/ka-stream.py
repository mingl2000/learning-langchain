from langchain_core.runnables import chain
from langchain_openai.chat_models import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


model = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat" 
)


template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)


@chain
def chatbot(values):
    prompt = template.invoke(values)
    for token in model.stream(prompt):
        yield token


for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)
