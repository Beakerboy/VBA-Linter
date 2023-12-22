from editorconfig import get_properties, EditorConfigError
from typing import Type, TypeVar

T = TypeVar('T', bound='ConfigHelper')

class ConfigHelper:
    def get_property(filename: str, property_name: str):
        try:
            options: dict = get_properties(filename)
        except EditorConfigError:
            print("Error occurred while getting EditorConfig properties")
        else:
            for key, value in options.items():
                if (key == property_name):
                    return value
