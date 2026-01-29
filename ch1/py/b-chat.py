from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
model = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat" 
)



prompt = [HumanMessage("What is the capital of France?")]

response = model.invoke(prompt)
print(response.content)
