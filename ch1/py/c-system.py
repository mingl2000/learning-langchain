from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai.chat_models import AzureChatOpenAI

model = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat" 
)

system_msg = SystemMessage(
    "You are a helpful assistant that responds to questions with three exclamation marks."
)
human_msg = HumanMessage("What is the capital of France?")

response = model.invoke([system_msg, human_msg])
print(response.content)
