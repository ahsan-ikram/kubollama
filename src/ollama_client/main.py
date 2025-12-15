from ollama_client.ollama import Ollama


def main() -> None:
    ollama: Ollama = Ollama()

    # REPL style prompting
    while True:
        print("Type '/bye' to exit.")
        prompt: str = input("User prompt: ")
        if prompt == "/bye":
            print("Exiting the REPL. Good bye!")
            break
        result: str = ollama.talk(prompt)
        print(f"User: {prompt}\nOllama:", result)


if __name__ == "__main__":
    main()
