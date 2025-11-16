import os

import requests
import json
import time

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")


def call_ollama(prompt, model="smollm:135m"):
    url = f"{OLLAMA_URL}/api/generate"
    payload = {"model": model, "prompt": prompt}

    print("[INFO] Attempting to connect to Ollama at:", url)
    print("[INFO] Sending generation request...")
    try:
        response = requests.post(url, json=payload, stream=True, timeout=50)
    except Exception as e:
        print("[ERROR] Connection failed during POST:", str(e))
        raise

    print("[INFO] Response status:", response.status_code)

    if response.status_code != 200:
        print("[ERROR] Server returned:", response.text)
        raise Exception(f"Error {response.status_code}: {response.text}")

    # --- Stream parsing ---
    print("[INFO] Reading streamed response...")
    output = ""
    line_count = 0

    for line in response.iter_lines():
        if not line:
            continue

        line_count += 1
        decoded = line.decode("utf-8")

        # Logging each line (helpful for debugging streaming issues)
        print(f"[STREAM] {decoded}")

        try:
            data = json.loads(decoded)
            if "response" in data:
                output += data["response"]
        except json.JSONDecodeError:
            print("[WARN] Could not decode JSON:", decoded)

    print(f"[INFO] Finished streaming. Lines received: {line_count}")
    print("[INFO] Final output length:", len(output))

    return output.strip()


def handshake_ollama() -> str:
    try:
        t0 = time.time()
        health = requests.get(OLLAMA_URL)
    except Exception as e:
        print("[ERROR] Cannot reach Ollama server:", str(e))
        raise Exception("Ollama server is not healthy")

    return f"Ollama handshake OK (HTTP {health.status_code}) in {time.time()-t0:.2f}s"
