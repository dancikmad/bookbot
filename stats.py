from typing import Dict, List


def get_num_words(text: str) -> int:

    words = text.split()
    num_words = len(words)
    return num_words


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_dictionary(stats: Dict[str, int]) -> List[Dict[str, int]]:
    sorted_dictionary: List[Dict[str, int]] = []
    for key, value in stats.items():
        sorted_dictionary.append({"character": key, "count": value})
    sorted_data = sorted(sorted_dictionary, key=lambda x: x["count"])

    return sorted_data
