
# Define state

from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: List[BaseMessage]

# Azure OpenAI LLM
from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    model="gpt-5.2-chat" 
)

#Define a tool
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


# Tool node
from langgraph.prebuilt import ToolNode

tool_node = ToolNode([multiply])

# Agent function
from langchain_core.messages import AIMessage

def agent_fn(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    return {
        "messages": state["messages"] + [response]
    }

# Conditional edge

def should_continue(state: AgentState):
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "continue"
    return "end"

# Build the LangGraph agent

from langgraph.graph import StateGraph, END

builder = StateGraph(AgentState)

builder.add_node("agent", agent_fn)
builder.add_node("tools", tool_node)

builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)

builder.add_edge("tools", "agent")
builder.set_entry_point("agent")

graph = builder.compile()


# Run it
from langchain_core.messages import HumanMessage

result = graph.invoke(
    {
        "messages": [
            HumanMessage(content="What is 7 multiplied by 8?")
        ]
    }
)

print(result["messages"][-1].content)

