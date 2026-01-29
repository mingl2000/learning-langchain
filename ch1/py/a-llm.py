from langchain_openai import AzureChatOpenAI
model = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat" 
)
response = model.invoke("is The sky blue most of the time in california daytime?")
print(response.content)
