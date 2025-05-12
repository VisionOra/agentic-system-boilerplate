"""Define the configurable parameters for the index graph."""

from __future__ import annotations

from dataclasses import dataclass, field

from langchain_openai import ChatOpenAI

from src.shared.configuration import BaseConfiguration

# This file contains sample documents to index, based on the following LangChain and LangGraph documentation pages:
# - https://python.langchain.com/v0.3/docs/concepts/
# - https://langchain-ai.github.io/langgraph/concepts/low_level/
DEFAULT_DOCS_FILE = "src/sample_docs.json"


@dataclass(kw_only=True)
class IndexConfiguration(BaseConfiguration):
    """Configuration class for indexing and retrieval operations.

    This class defines the parameters needed for configuring the indexing and
    retrieval processes, including embedding model selection, retriever provider choice, and search parameters.
    """
    llm_model: str = field(
        default="gpt-3.5-turbo",
        metadata={
            "description": "The language model to use for generating responses."
        },
    )
    
    @property
    def llm(self) -> ChatOpenAI:
        """Get the LLM instance.
        
        Returns:
            ChatOpenAI: The configured LLM.
        """
        return ChatOpenAI(model=self.llm_model)
    
    