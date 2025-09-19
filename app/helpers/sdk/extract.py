from typing import Any, List


def extract_items(response: Any, source: str = "items") -> List[Any]:
    """
    Extracts a list from the given source (key or attribute) in response.

    Parameters:
        response (Any): The object or dictionary to extract from.
        source (str): The key (for dict) or attribute (for objects) to extract.
                      Defaults to 'items'.

    Returns:
        List[Any]: Extracted list or empty list if source is missing.
    """
    if isinstance(response, dict):
        return response.get(source, []) or []
    return getattr(response, source, []) or []
