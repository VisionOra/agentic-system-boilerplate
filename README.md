# SimpleChatbot with LangGraph

A lightweight, standalone chatbot built using LangGraph. This project provides a clean, simple implementation of a conversational agent that can be easily extended or customized.

## Overview

This chatbot provides a straightforward implementation of a conversational agent using LangGraph. It handles:

- Message processing
- Response generation
- Conversation state management

The design prioritizes simplicity and maintainability, making it an excellent starting point for more complex conversational applications.

## Prerequisites

- Python 3.9+ (required)
- [Poetry](https://python-poetry.org/docs/#installation) (recommended for dependency management)

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd simple-chatbot
```

### 2. Environment Setup

1. Create your environment file:

```bash
cp .env.example .env
```

2. Configure your API keys in the `.env` file:
   ```
   # LLM API
   OPENAI_API_KEY=your_openai_key
   ```

### 3. Install Python Dependencies

Using Poetry (recommended):
```bash
poetry install
poetry shell
```

OR using pip:
```bash
pip install -e .
```

## Running the Chatbot

### Start the LangGraph Development Server

```bash
langgraph dev
```

This will start the LangGraph development server, which provides a web interface to interact with your chatbot and view the graph execution.

### Run Using Python

You can also use the chatbot directly in Python:

```python
from src.index_graph import graph as chatbot_graph
from langchain_core.messages import HumanMessage

# Create a message
messages = [HumanMessage(content="Hello, how are you today?")]

# Invoke the chatbot
result = await chatbot_graph.ainvoke({"messages": messages})

# Print the response
print(result["messages"][-1].content)
```

## Project Structure

- `src/`: Main source code
  - `index_graph/`: Core chatbot components
    - `configuration.py`: Configuration settings and LLM setup
    - `graph.py`: Main graph definition and message handler
    - `state.py`: State management for the chat
  - `shared/`: Shared utilities and components
- `tests/`: Test suite

## Configuration Options

The chatbot can be configured through the `IndexConfiguration` class:

- `llm_model`: The language model to use (default: "gpt-3.5-turbo")

You can adjust these settings when invoking the graph:

```python
from langchain_core.runnables import RunnableConfig

config = RunnableConfig(
    configurable={
        "llm_model": "gpt-4o",
    }
)

result = await chatbot_graph.ainvoke({"messages": messages}, config)
```

## Development

### Run LangGraph Developer Mode

```bash
langgraph dev --allow-blocking
```

This starts the LangGraph development server, allowing you to visualize and interact with your graph.

### Run tests:

```bash
poetry run pytest
```

## Extending the Chatbot

The simple architecture makes it easy to extend the chatbot with additional capabilities:

1. **Add Memory**: Implement persistent storage to maintain conversation history
2. **Integrate Tools**: Add function-calling capabilities for external API interactions
3. **Enhance Processing**: Implement pre/post-processing for more sophisticated message handling
4. **Custom Routing**: Add conditional logic to route messages to different handlers

## Troubleshooting

- **API key errors**: Ensure the required API keys are properly configured in your `.env` file
- **Model errors**: Check that you're using a supported model for your API key
- **Poetry issues**: Try running `poetry lock --no-update` followed by `poetry install`