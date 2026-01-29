from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel


class AnswerWithJustification(BaseModel):
    """An answer to the user's question along with justification for the answer."""

    answer: str
    """The answer to the user's question"""
    justification: str
    """Justification for the answer"""


model = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat",
    temperature=0 
)
structured_llm = llm.with_structured_output(AnswerWithJustification)

response = structured_llm.invoke(
    "What weighs more, a pound of bricks or a pound of feathers")
print(response)
