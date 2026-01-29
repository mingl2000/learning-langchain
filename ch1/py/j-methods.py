from langchain_openai.chat_models import AzureChatOpenAI

model = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat" 
)

completion = model.invoke("Hi there!")
# Hi!

completions = model.batch(["Hi there!", "Bye!"])
# ['Hi!', 'See you!']

for token in model.stream("Bye!"):
    print(token)
    # Good
    # bye
    # !
