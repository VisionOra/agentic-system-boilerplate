"""Simple chatbot using LangGraph."""

from typing import Optional

from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph
from langchain_core.messages import AIMessage

from src.index_graph.configuration import IndexConfiguration
from src.index_graph.state import IndexState


async def generate_response(
    state: IndexState, *, config: Optional[RunnableConfig] = None
) -> IndexState:
    """Generate a response to user messages.

    :param IndexState state: The current state
    :param Optional[RunnableConfig] config: Configuration, defaults to None
    :return IndexState: Updated state with response
    """
    # Get configuration
    configuration = IndexConfiguration.from_runnable_config(config) if config else IndexConfiguration()
    
    # Only process if there are messages to respond to
    if state.messages:
        # Use the messages directly
        response = await configuration.llm.ainvoke(state.messages)
        
        # Return updated state with the response added to messages
        return IndexState(
            messages=state.messages + [response]
        )
    
    # If no messages, just return the original state
    return state


# Define the graph
builder = StateGraph(IndexState, config_schema=IndexConfiguration)

# Add node
builder.add_node("generate_response", generate_response)

# Add edges
builder.add_edge(START, "generate_response")
builder.add_edge("generate_response", END)

# Compile into a graph object that you can invoke and deploy.
graph = builder.compile()
graph.name = "SimpleChatbot"
