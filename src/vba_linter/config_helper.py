from editorconfig import get_properties, EditorConfigError

filename = "/linter.py"

try:
    options = get_properties(filename)
except EditorConfigError:
    print("Error occurred while getting EditorConfig properties")
else:
    for key, value in options.items():
        print("%s=%s" % (key, value))
        