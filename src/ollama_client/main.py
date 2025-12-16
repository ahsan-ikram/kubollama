from ollama_client.ollama import Ollama
import time

def main() -> None:
    ollama: Ollama = Ollama()

    # REPL style prompting
    while True:
        try:
            print("Type '/bye' to exit.")
            prompt: str = input("User prompt: ")
            if prompt == "/bye":
                print("Exiting the REPL. Good bye!")
                break
            result: str = ollama.talk(prompt)
            print(f"User: {prompt}\nOllama:", result)
        except EOFError:
            # When the container starts, stdin is not open, which causes an EOFError.
            # We wait for a TTY to be attached, which will open stdin.
            time.sleep(1)

if __name__ == "__main__":
    main()
