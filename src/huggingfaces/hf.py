from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

def stream(prompt:str):
    """
    Stream text generation from a given prompt using an inference client.

    Parameters
    ----------
    prompt : str
        The prompt text to generate responses from.

    Returns
    -------
    Any
        The response from the text generation, streaming the output.
    """
    client = InferenceClient(os.getenv("HF_ENDPOINT"))
    return client.text_generation(prompt, max_new_tokens=1024, stream=True)