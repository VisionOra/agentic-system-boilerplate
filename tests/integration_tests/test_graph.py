import pytest
from langchain_core.runnables import RunnableConfig
from langsmith import expect, unit
from langchain_core.messages import HumanMessage

from src.index_graph import graph as chatbot_graph


@pytest.mark.asyncio
@unit
async def test_chatbot() -> None:
    """Test the simple chatbot functionality."""
    # Create a config for the test
    config = RunnableConfig(
        configurable={
            "llm_model": "gpt-3.5-turbo",
        }
    )
    
    # Test a basic message exchange
    user_message = HumanMessage(content="Hi! How are you?")
    result = await chatbot_graph.ainvoke(
        {"messages": [user_message]},
        config,
    )
    
    # Verify we received a response
    expect(len(result["messages"])).to_be(2)  # Original message + response
    expect(result["messages"][0].content).to_be("Hi! How are you?")
    # Verify the response is not empty
    expect(result["messages"][1].content).not_to_be("")
