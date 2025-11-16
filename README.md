# Ollam Client
This project is a custom client meant for experimentation. It creates a minimal python based client. It is able to communicate with Ollama offline models. 

The application is dockerized

- Can communicate to hostbased or external Ollama server
- Bundled as service with ollama as docker (see docker-compose.yml)

## LLM Model
- Ollama
- LLM model smollm:135m (Small)

## Using Poetry 
poetry install

poetry run python -m ollama_client.main

## Using Docker
docker build -t ollama-client .

### Use Ollama Server on host
docker run --rm -e OLLAMA_URL=http://host.docker.internal:11434 ollama-client


### Use Ollama server within a new docker

docker-compose down -v       
docker-compose up --build