import json
from typing import Dict

def generate_module(topic: str, length: int) -> Dict:
    """Create a simple module outline for the given topic."""
    days = [f"Day {i+1}: Learn about {topic}" for i in range(length)]
    return {"topic": topic, "length": length, "schedule": days}


def save_module(module: Dict, path: str) -> None:
    """Save the module dictionary to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(module, f, indent=2)

