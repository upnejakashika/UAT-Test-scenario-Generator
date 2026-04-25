import requests

OLLAMA_URL = "http://ollama:11434/api/generate"

def call_llm(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")


def extract_requirements(text):
    prompt = f"""
    Extract the following from the given SRS:
    - Modules
    - Functional Requirements
    - User Roles

    Return structured output.

    TEXT:
    {text[:3000]}
    """
    return call_llm(prompt)


def generate_test_scenarios(data):
    prompt = f"""
    Generate test scenarios under:
    1. UI/UX
    2. Functional Testing
    3. Role-Based Testing

    Based on:
    {data}
    """
    return call_llm(prompt)
