import argparse
import os
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ruleset", nargs='?', default='.',
                        help="Configuration file of linting rules.")
    parser.add_argument("directory", default='.',
                        help="The input or output directory.")
    args = parser.parse_args()
    linter = Linter()
    file_list = find_files(args.directory)
    full_results: dict[str, list] = {}
    for file in file_list:
        code = open(file, 'r').read()
        dir = RuleDirectory()
        dir.load_all_rules()
        results = linter.lint(dir, code)
        if len(results) > 0:
            full_results[file] = results


def find_files(path: str) -> list:
    files = []
    obj = os.scandir(path)
    for entry in obj:
        if entry.is_dir():
            files.extend(find_files(entry.name))
        else:
            # if extension is bas, cls. or frm
            files.append(entry)
    return files


if __name__ == '__main__':
    main()
