from ollama_client.client import call_ollama, handshake_ollama


def main() -> None:
    print(f"{handshake_ollama()} ")
    result = call_ollama("Hello ollama")
    print("Ollama response:", result)


if __name__ == "__main__":
    main()
