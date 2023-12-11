import argparse
import os
import sys
from linter import Linter


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ruleset", nargs='?', default='.',
                        help="Configuration file of linting rules.")
    parser.add_argument("directory", default='.',
                        help="The input or output directory.")
    args = parser.parse_args()
    linter = Linter()
    file_list = find_files(args.directory)
    full_results = []
    for file in file_list:
        code = open(file, 'r').read()
        results = linter.lint(code)
        if len(results) > 0:
            full_results[file] = results
    


def find_files(path: str) -> list:
    files = []
    obj = os.scandir(args.directory)
    for entry in obj:
        if entry.is_dir():
            files.extend(find_files(entry))
        else:
            files.append(entry)


if __name__ == '__main__':
    main(sys.argv)
