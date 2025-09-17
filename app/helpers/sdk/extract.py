from typing import Any, List


def extract_items(response: Any) -> List:
    if isinstance(response, dict):
        return response.get("items") or []  # fallback to []
    return getattr(response, "items", []) or []  # fallback to []
