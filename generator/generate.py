"""Simple curriculum module generator."""

import os
import json
from typing import Dict

import openai


def generate_module(topic: str, length: int = 5) -> Dict:
    """Generate a micro-curriculum module using OpenAI."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set")
    openai.api_key = api_key

    prompt = f"Create a {length}-day STEM curriculum about {topic}."\
             " Provide slides, worksheets, and a mini-project." 

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    content = response.choices[0].message["content"]
    return {"topic": topic, "content": content}


def save_module(module: Dict, path: str) -> None:
    with open(path, "w") as f:
        json.dump(module, f, indent=2)


if __name__ == "__main__":
    module = generate_module("Intro to Coding")
    save_module(module, "../data/sample_module.json")
