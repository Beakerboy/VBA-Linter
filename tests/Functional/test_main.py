import pytest
import random
import string
from pathlib import Path
from pytest_mock import MockerFixture
from _pytest.capture import CaptureFixture
from vba_linter.__main__ import main
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory


@pytest.fixture(autouse=True)
def run_around_tests() -> None:
    global files
    files = []
    # Code that will run before your test, for example:
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    for file in files:
        delete_code(file)
    files = []


def save_code(code: str) -> str:
    file_name = create_filename(ext='.bas')
    p = Path(file_name)
    with p.open(mode='a') as fi:
        fi.write(code)
    return file_name


def create_filename(num: int = 16, ext: str = ".txt") -> str:
    chars = ""
    for i in range(num):
        chars += random.choice(string.ascii_lowercase)
    file_name = chars + ext
    return "tests/Functional/" + file_name


def delete_code(file_name: str) -> None:
    p = Path(file_name)
    p.unlink()


function = 'Supercalifragilisticexpialidocious'
worst_practice = (
    'Attribute VB_Name = "Foo"\r\n' +
    'Public Function ' + function +
    ' ( atrocious ,  precocious, indubitably ) \n' +
    ' \r\n' +
    '\r\n' +
    '\n' +
    '\r\n' +
    'I = (2 + 1)\n' +
    '    foo_val=6\r\n'
    '    Let BarVal  =  (7 + 2) / 3\r\n'
    'End Function\n' +
    '\r\n' +
    'sub O()\r\n' +
    'End Sub\r\n' +
    '\r\n'
)
pretty = (
    'Attribute VB_Name = "Foo"\r\n' +
    'Public Function ' + function +
    ' ( atrocious ,  precocious, indubitably ) \r\n' +
    ' \r\n' +
    '\r\n' +
    '\r\n' +
    'I = (2 + 1)\r\n' +
    '    foo_val=6\r\n'
    '    Let BarVal  =  (7 + 2) / 3\r\n'
    'End Function\r\n' +
    '\r\n' +
    'sub O()\r\n' +
    'End Sub\r\n'
)


worst_expected = """\
%s:2:1: E505 Optional public
%s:2:51: E121 Excess whitespace before '('
%s:2:53: E124 Excess whitespace after '('
%s:2:63: E141 Excess whitespace before ','
%s:2:66: E144 Excess whitespace after ','
%s:2:80: W501 line too long (92 > 79 characters)
%s:2:90: E131 Excess whitespace before ')'
%s:2:92: E305 Trailing whitespace
%s:2:92: E400 incorrect line ending
%s:3:1: W310 Blank line contains whitespace
%s:5:0: E400 incorrect line ending
%s:6:0: W303 Too many blank lines (3)
%s:7:1: W201 Missing let
%s:7:11: E400 incorrect line ending
%s:8:5: W201 Missing let
%s:8:12: E150 Missing whitespace before '='
%s:8:13: E153 Missing whitespace after '='
%s:9:5: W202 Optional let
%s:9:16: E151 Excess whitespace before '='
%s:9:19: E154 Excess whitespace after '='
%s:10:12: E400 incorrect line ending
%s:12:1: E220 Keyword not capitalized
%s:12:1: W510 Missing visibility
%s:14:1: W391 blank line at end of file
24 Errors in 1 File
"""


def test_worst_file_all(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    file_name = save_code(worst_practice)
    files.append(file_name)
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "-x",
            "tests/Functional",
            "all"
        ],
    )
    with pytest.raises(SystemExit):
        main()
    files.append(file_name + ".pretty")
    captured = capsys.readouterr()
    full_path = ("/home/runner/work/VBA-Linter/VBA-Linter/" + file_name)
    expected = worst_expected.replace("%s", full_path)
    assert captured.err == expected
    f = open(file_name + ".pretty", "r", newline='')
    pretty_file = f.read()
    assert pretty_file == pretty


def test_worst_file_std(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    file_name = save_code(worst_practice)
    files.append(file_name)
    full_path = ("/home/runner/work/VBA-Linter/VBA-Linter/" + file_name)
    expected = """\
%s:2:51: E121 Excess whitespace before '('
%s:2:53: E124 Excess whitespace after '('
%s:2:63: E141 Excess whitespace before ','
%s:2:66: E144 Excess whitespace after ','
%s:2:90: E131 Excess whitespace before ')'
%s:2:92: E305 Trailing whitespace
%s:2:92: E400 incorrect line ending
%s:5:0: E400 incorrect line ending
%s:7:11: E400 incorrect line ending
%s:8:12: E150 Missing whitespace before '='
%s:8:13: E153 Missing whitespace after '='
%s:9:16: E151 Excess whitespace before '='
%s:9:19: E154 Excess whitespace after '='
%s:10:12: E400 incorrect line ending
%s:12:1: E220 Keyword not capitalized
15 Errors in 1 File
""".replace("%s", full_path)  # noqa
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "tests/Functional",
        ],
    )
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert captured.err == expected


def test_worst_silent(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    """
    Ensure that -q still fails, but has no output.
    """
    file_name = save_code(worst_practice)
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "-q",
            "tests/Functional",
            "all"
        ],
    )
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert captured.err == ""
    delete_code(file_name)


def test_worst_zero(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    """
    Ensure that --exit-zero returns the same output, but does not trigger
    an exception
    """
    file_name = save_code(worst_practice)
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "--exit-zero",
            "tests/Functional",
            "all"
        ],
    )
    main()
    captured = capsys.readouterr()
    full_path = ("/home/runner/work/VBA-Linter/VBA-Linter/" + file_name)
    expected = worst_expected.replace("%s", full_path)
    assert captured.err == expected
    delete_code(file_name)


def test_best_practice(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    best_practice = (
        'Attribute VB_Name = "Foo"\r\n' +
        'Option Explicit\r\n' +
        '\r\n' +
        'Public Function Foo(val1, val2, val3)\r\n' +
        '\r\n' +
        '\r\n' +
        '    i = (2 + 1)\r\n' +
        '    foo_val = 6\r\n'
        '    bar_val = 7\r\n'
        'End Function\r\n' +
        '\r\n' +
        'Private Sub Opens()\r\n' +
        'End Sub\r\n'
    )
    file_name = save_code(best_practice)
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "-x",
            "tests/Functional",
        ],
    )
    main()
    captured = capsys.readouterr()
    assert captured.err == ""
    f = open(file_name + ".pretty", "r", newline='')
    pretty_file = f.read()
    assert pretty_file == best_practice
    delete_code(file_name + ".pretty")
    delete_code(file_name)


worst_practice1 = (
    'Attribute VB_Name = "Foo"\r\n' +
    '\' noqa: 400\r\n' +
    'Public Function ' + function +
    ' ( atrocious ,  precocious, indubitably ) \n' +
    ' \r\n' +
    '\r\n' +
    '\n' +
    '\r\n' +
    'I = (2 + 1)\n' +
    '    foo_val=6\r\n'
    '    Let BarVal  =  (7 + 2) / 3\r\n'
    'End Function\n' +
    '\r\n' +
    'sub O()\r\n' +
    'End Sub\r\n' +
    '\r\n'
)


def test_ignore(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    file_name = save_code(worst_practice1)
    files.append(file_name)
    full_path = ("/home/runner/work/VBA-Linter/VBA-Linter/" + file_name)
    dir = RuleDirectory()
    linter = Linter()
    dir.load_standard_rules()
    results = linter.lint(dir, full_path)
    assert len(results) == 15
    expected = """\
%s:3:51: E121 Excess whitespace before '('
%s:3:53: E124 Excess whitespace after '('
%s:3:63: E141 Excess whitespace before ','
%s:3:66: E144 Excess whitespace after ','
%s:3:90: E131 Excess whitespace before ')'
%s:3:92: E305 Trailing whitespace
%s:9:12: E150 Missing whitespace before '='
%s:9:13: E153 Missing whitespace after '='
%s:10:16: E151 Excess whitespace before '='
%s:10:19: E154 Excess whitespace after '='
%s:13:1: E220 Keyword not capitalized
11 Errors in 1 File
""".replace("%s", full_path)  # noqa
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "tests/Functional",
        ],
    )
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert captured.err == expected
