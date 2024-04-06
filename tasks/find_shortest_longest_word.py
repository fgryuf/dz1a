from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    inp = text.split()
    if len(inp) == 0:
        return (None, None)
    return (min(inp, key=len), max(inp, key=len))

print(find_shortest_longest_word('hello there, general kenobi'))