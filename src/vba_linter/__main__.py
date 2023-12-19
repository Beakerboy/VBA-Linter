import argparse
from pathlib import Path
import sys
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory


def main() -> None:
    parser = argparse.ArgumentParser()
    # parser.add_argument("ruleset", nargs='?', default='.',
    #                     help="Configuration file of linting rules.")
    parser.add_argument("directory", default='.',
                        help="The source directory.")
    args = parser.parse_args()
    linter = Linter()
    path = Path(args.directory).resolve()
    file_list = find_files(path)
    full_results: dict[str, list] = {}
    num_errors = 0
    for file_name in file_list:
        dir = RuleDirectory()
        dir.load_all_rules()
        results = linter.lint(dir, file_name)
        if len(results) > 0:
            full_results[file_name] = results
    for file_name, file_results in full_results.items():
        num_errors += len(file_results)
        for error in file_results:
            msg = dir.get_rule(error[2]).create_message(error)
            print(str(file_name) + msg, file=sys.stderr)
    num_files = len(file_list)
    plural_e = "" if num_errors < 2 else "s"
    plural_f = "" if num_files < 2 else "s"
    data = (num_errors, plural_e, num_files, plural_f)
    print(
        "%s Error%s in %s File%s" % data,
        file=sys.stderr
    )

    exit_code = 1 if num_errors > 0 else 0
    sys.exit(exit_code)


def find_files(path: Path) -> list:
    files = []
    for child in path.rglob("*"):
        if child.suffix in [".bas", ".cls", ".frm"]:
            files.append(child)
    return files


if __name__ == '__main__':
    main()
