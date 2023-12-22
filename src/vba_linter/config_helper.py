from editorconfig import get_properties, EditorConfigError

filename: str = "/linter.py"

try:
    options: dict = get_properties(filename)
except EditorConfigError:
    print("Error occurred while getting EditorConfig properties")
else:
    for key, value in options.items():
        print("%s=%s" % (key, value))