import argparse
import os
from pathlib import Path
import sys
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory


def main() -> None:
    parser = argparse.ArgumentParser()
    # parser.add_argument("ruleset", nargs='?', default='.',
    #                     help="Configuration file of linting rules.")
    parser.add_argument("directory", default='.',
                        help="The input or output directory.")
    args = parser.parse_args()
    linter = Linter()
    path = Path(args.directory).resolve()
    file_list = find_files(path)
    full_results: dict[str, list] = {}
    for file_name in file_list:
        dir = RuleDirectory()
        dir.load_all_rules()
        results = linter.lint(dir, file_name)
        if len(results) > 0:
            full_results[file_name] = results
    for file_name, file_results in full_results.items():
        for error in file_results:
            msg = dir.get_rule(error[2]).create_message(error)
            print(file_name + msg, file=sys.stderr)


def find_files(path: Path) -> list:
    files = []
    for child in p.iterdir():
        if child.is_dir():
            # if extension is bas, cls. or frm
            files.append(child)
    return files


if __name__ == '__main__':
    main()
