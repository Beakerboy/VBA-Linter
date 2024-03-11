import re


def is_snake_case(cls: Type[T], name: str) -> bool:
    pattern = '(^[a-z]{1}$)|([a-z]+(_[a-z]+)*$)'
    return cls.text_matches(pattern, name)


def is_camel_case(cls: Type[T], name: str) -> bool:
    """
    Also known as lowerCamelCase.
    """
    pattern = '(^[a-z]{1}$)|([a-z]{2,}([a-zA-Z]([a-z])+)*$)'
    return cls.text_matches(pattern, name)


def is_pascal_case(cls: Type[T], name: str) -> bool:
    """
    Also known as UpperCamelCase.
    """
    pattern = '(^[a-z]{1}$)|(([A-Z]([a-z])+)*$)'
    return cls.text_matches(pattern, name)


def text_matches(cls: Type[T], pattern: str, name: str) -> bool:
    match = re.match(pattern, name)
    if match:
        return True
    return False
