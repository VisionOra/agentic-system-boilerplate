# RAG Research Agent Template

A powerful RAG (Retrieval-Augmented Generation) research agent template built with LangGraph. This template provides a framework for building advanced retrieval-augmented generation systems.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.9+ (required)
- [Poetry](https://python-poetry.org/docs/#installation) (recommended for dependency management)

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd rag-research-agent-template
```

### 2. Environment Setup

1. Create your environment file:

```bash
cp .env.example .env
```

2. Configure your API keys in the `.env` file:
   ```
   # LLM APIs
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   FIREWORKS_API_KEY=your_fireworks_key
   
   # Pinecone
   PINECONE_API_KEY=your_pinecone_key
   PINECONE_INDEX_NAME=your_index_name
   ```

### 3. Start the Infrastructure Services

Using Docker Compose to start Elasticsearch and MongoDB:

```bash
docker-compose up -d
```

This starts:
- **Elasticsearch**: Available at http://localhost:9200
- **MongoDB**: Available at mongodb://admin:password@localhost:27017

### 4. Verify Services

Check if Elasticsearch is running:
```bash
curl http://localhost:9200
```

Check if MongoDB is running:
```bash
docker exec -it mongodb mongosh -u admin -p password --eval "db.serverStatus().ok"
```

### 5. Install Python Dependencies

Using Poetry (recommended):
```bash
poetry install
poetry shell
```

OR using pip:
```bash
pip install -e .
```

### 6. Run Tests

Verify your installation is working correctly:
```bash
make test
```

## Project Structure

- `src/`: Main source code
  - `retrieval_graph/`: Components for retrieval functionality
  - `index_graph/`: Components for indexing functionality
  - `shared/`: Shared utilities and components
- `tests/`: Test suite
- `docker-compose.yml`: Docker configuration for Elasticsearch and MongoDB

## LLM Provider Options

The application supports multiple LLM providers:
- OpenAI
- Anthropic
- Fireworks

## Retrieval Options

Multiple retrieval backends are supported:
- Elasticsearch (local or cloud)
- MongoDB
- Pinecone

## Environment Variables Reference

```
# Project Configuration
LANGSMITH_PROJECT=rag-research-agent

# LLM APIs
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
FIREWORKS_API_KEY=your_fireworks_key

# Elasticsearch Configuration
ELASTICSEARCH_URL=http://localhost:9200
ELASTICSEARCH_USER=
ELASTICSEARCH_PASSWORD=
ELASTICSEARCH_CLOUD=false

# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX_NAME=your_index_name

# MongoDB Configuration
MONGODB_URI=mongodb://admin:password@localhost:27017
```

## Docker Services

The included Docker Compose file sets up:

1. **Elasticsearch**:
   - Version: 8.11.1
   - Configuration: Single node setup with security disabled
   - Ports: 9200, 9300
   - Data persistence via Docker volume

2. **MongoDB**:
   - Version: 7.0
   - Credentials: admin/password
   - Port: 27017
   - Data persistence via Docker volume

## Development

### Run Langchain Studio

```bash
langgraph dev --allow-blocking
```

### Run tests:
```bash
make test
```

Run tests with watch mode:
```bash
make test_watch
```

## Troubleshooting

- **Elasticsearch not starting**: Check Docker logs with `docker logs elasticsearch`
- **MongoDB connection issues**: Verify credentials and connection string in your `.env` file
- **API key errors**: Ensure all required API keys are properly configured in your `.env` file
- **Poetry issues**: Try running `poetry lock --no-update` followed by `poetry install`
# agentic-system-boilerplate
