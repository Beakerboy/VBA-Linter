import argparse
from pathlib import Path
import sys
from typing import Dict
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--fix", action="store_true",
                        help="Fix whitespace errors.")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Do not print failures.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Display more information.")
    parser.add_argument("-i", "--ignore", help="ignore a set of rules.")
    msg = "Use the exit status code 0 even if there are errors."
    parser.add_argument("--exit-zero", action="store_true",
                        help=msg)
    parser.add_argument("directory", default='.',
                        help="The source directory.")
    parser.add_argument("ruleset", nargs='?', default='default',
                        help="Configuration file of linting rules.")
    args = parser.parse_args()
    linter = Linter()
    path = Path(args.directory).resolve()
    file_list = find_files(path)
    full_results: Dict[str, list] = {}
    num_errors = 0
    for file_name in file_list:
        dir = RuleDirectory()
        if args.ruleset == "all":
            dir.load_all_rules()
        elif args.ruleset == "default":
            dir.load_standard_rules()
        else:
            # check that file is yml
            # add rules
            ...
        if args.ignore != "":
            dir.remove_rule(args.ignore)
        results = linter.lint(dir, file_name)
        if len(results) > 0:
            full_results[file_name] = results
        if args.fix:
            pretty_code = linter.get_pretty_code()
            p = Path(str(file_name) + ".pretty")
            with p.open(mode='a') as fi:
                fi.write(pretty_code)
    output = ""
    for file_name, file_results in full_results.items():
        num_errors += len(file_results)
        for error in file_results:
            class_id = error[2][:3]
            msg = dir.get_rule(class_id).create_message(error)
            output += str(file_name) + msg + "\n"
    num_files = len(file_list)
    plural_e = "" if num_errors < 2 else "s"
    plural_f = "" if num_files < 2 else "s"
    data = (num_errors, plural_e, num_files, plural_f)
    if num_errors > 0 or args.verbose:
        output += "%s Error%s in %s File%s" % data
    if not args.quiet and output != "":
        print(output, file=sys.stderr)
    if num_errors > 0 and not args.exit_zero:
        exit_code = 1
        sys.exit(exit_code)


def find_files(path: Path) -> list:
    files = []
    for child in path.rglob("*"):
        if child.suffix in [".bas", ".cls", ".frm"]:
            files.append(child)
    return files


if __name__ == '__main__':
    main()
