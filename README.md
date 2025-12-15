# Ollama on Kubernetes

This project is a hands-on learning experience for dockerizing an Ollama instance with a pre-loaded model and deploying it to a Kubernetes cluster along with a simple client application.

The core of this project is a simple REPL (Read-Eval-Print Loop) application that takes prompts from the user and communicates with the Ollama service to get a response from a Large Language Model.

## Key Learnings & Technologies

This project explores the following concepts and technologies:

*   **Docker**: Creating custom Docker images for both the Ollama server and the Python client application using multi-stage builds.
*   **Ollama**: Running Ollama in a container and pre-loading a specific model (`gemma3:1b`) into the image to avoid download times on startup.
*   **Python**: A simple Python client with a REPL interface to interact with the Ollama API.
*   **Kubernetes**: Deploying the multi-container application to a Kubernetes cluster using `Deployment` and `Service` manifests. It's configured to be compatible with local clusters like `kind`.
*   **uv**: Using `uv` as a fast Python package installer and manager.

## Project Structure

The project is organized as follows:

```
.
├── Dockerfile.app         # Dockerfile for the Python REPL client
├── Dockerfile.ollama      # Dockerfile for the Ollama server with a pre-loaded model
├── docker-compose.yml     # For local development and orchestration
├── k8s/                     # Kubernetes manifests
│   ├── app.yml
│   └── ollama.yml
├── src/
│   └── ollama_client/       # Python source code for the REPL client
...
```

## Getting Started

You can run this project in three different ways: locally for development, using Docker Compose, or by deploying to a Kubernetes cluster.

### 1. Local Development

To run the REPL application directly on your machine for development:

1.  **Install the project in editable mode** (this makes the `ollama-k8s` package available in your environment):
    ```bash
    uv pip install -e .
    ```
2.  **Run the application**:
    ```bash
    uv run start
    ```
    This will start the REPL, and you can begin typing prompts. This setup requires a separate Ollama server running and accessible at `http://localhost:11434`.

### 2. Docker Compose

To run both the application and the Ollama server in Docker containers:

1.  **Build and start the services**:
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images and start both the `ollama` and `app` containers. The application will start in the foreground, and you can interact with it directly in your terminal.

### 3. Kubernetes (using kind)

To deploy the application to a local Kubernetes cluster using `kind`:

1.  **Create a `kind` cluster** (if you don't already have one):
    ```bash
    kind create cluster --name ollama-cluster
    ```

2.  **Build the Docker images**:
    The Kubernetes cluster needs access to the Docker images. First, build them using `docker-compose`:
    ```bash
    docker-compose build
    ```

3.  **Load the images into the `kind` cluster**:
    ```bash
    kind load docker-image ollama-k8s-ollama:dev --name ollama-cluster
    kind load docker-image ollama-k8s-app:dev --name ollama-cluster
    ```

4.  **Deploy the application to Kubernetes**:
    ```bash
    kubectl apply -f k8s/
    ```

5.  **Interact with the application**:
    The application container is running in a pod. To interact with it, you need to get a shell into the pod:

    *   Find the name of your app pod:
        ```bash
        kubectl get pods
        ```
        Look for a pod with a name like `app-deployment-...`.

    *   Get an interactive shell into the pod:
        ```bash
        kubectl exec -it <your-app-pod-name> -- bash
        ```

    *   Inside the pod's shell, run the REPL application:
        ```bash
        python -m ollama_client.main
        ```
