from huggingface_hub import InferenceClient
from dotenv import load_dotenv

import os

load_dotenv()

def stream(prompt):
    client = InferenceClient(os.getenv("HF_ENDPOINT"))
    return client.text_generation(prompt, max_new_tokens=1024, stream=True)