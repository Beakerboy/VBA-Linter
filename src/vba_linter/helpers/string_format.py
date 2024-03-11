import re


def is_snake_case(name: str) -> bool:
    pattern = '(^[a-z]{1}$)|([a-z]+(_[a-z]+)*$)'
    return text_matches(pattern, name)


def is_camel_case(name: str) -> bool:
    """
    Also known as lowerCamelCase.
    """
    pattern = '(^[a-z]{1}$)|([a-z]{2,}([a-zA-Z]([a-z])+)*$)'
    return text_matches(pattern, name)


def is_pascal_case(name: str) -> bool:
    """
    Also known as UpperCamelCase.
    """
    pattern = '(^[a-z]{1}$)|(([A-Z]([a-z])+)*$)'
    return text_matches(pattern, name)


def text_matches(pattern: str, name: str) -> bool:
    match = re.match(pattern, name)
    if match:
        return True
    return False
