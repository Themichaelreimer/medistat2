from typing import Callable, Set, List

"""
    This file implements a function tagging system, where functions can be tagged with
    one or more tags, and we can query functions by those tags.

    Example:

    @tag('test', 'unit', 'django')
    def test_foo():
        ...

    @tag('test', 'unit', 'airflow')
    def test_bar():
        ...

    >>> get_functions_by_tag('test')
    [test_foo, test_bar]
"""

__TAG_MAP: dict[str, set] = {}


def tag(*tags: str) -> Callable:
    def wrapper(f: Callable) -> Callable:
        for tag in tags:
            if tag not in __TAG_MAP:
                __TAG_MAP[tag] = set()

            __TAG_MAP[tag].add(f)
        return f

    return wrapper


def get_functions_by_tag(tag: str) -> Set[Callable]:
    """
    Returns all functions tagged with tag if they exist.
    If not, an empty set.

    :param tag: string tag
    :return: set of all tags tagged with tag
    """
    return __TAG_MAP.get(tag, set())


def get_functions_by_tags(*tags: str) -> Set[Callable]:
    result: Set[Callable] = set()
    for tag in tags:
        result = result.union(get_functions_by_tag(tag))
    return result


def get_all_tags() -> List[str]:
    """
    Returns all tags sorted alphabetically
    """
    result = list(__TAG_MAP.keys())
    result.sort()
    return result
