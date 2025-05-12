"""State management for the index graph."""

from dataclasses import dataclass, field
from typing import Annotated

from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages


# The index state defines the simple IO for the single-node index graph
@dataclass(kw_only=True)
class IndexState:
    """Represents the state for a simple chatbot.

    This class defines the structure of the chat state, which includes
    the messages exchanged between the user and the chatbot.
    """
    messages: Annotated[list[AnyMessage], add_messages] = field(default_factory=list)
    """Messages track the conversation between the user and the chatbot."""