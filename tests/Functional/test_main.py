import pytest
import random
import string
from pathlib import Path
from pytest_mock import MockerFixture
from _pytest.capture import CaptureFixture
from vba_linter.__main__ import main


files = []


@pytest.fixture(autouse=True)
def run_around_tests() -> None:
    files = []
    # Code that will run before your test, for example:
    # do something to check the existing files
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
    'Public Function ' + function +
    ' ( atrocious ,  precocious, indubitably ) \n' +
    '\n' +
    '\r\n' +
    '\r\n' +
    'I = (2 + 1)\n' +
    '    foo_val=6\r\n'
    '    Let BarVal  =  7\r\n'
    'End Function\n' +
    '\r\n' +
    'Sub O()\r\n' +
    'End Sub\r\n' +
    '\r\n'
)
pretty = (
    'Public Function ' + function +
    ' ( atrocious ,  precocious, indubitably ) \r\n' +
    '\r\n' +
    '\r\n' +
    'I = (2 + 1)\r\n' +
    '    foo_val=6\r\n'
    '    Let BarVal  =  7\r\n'
    'End Function\r\n' +
    '\r\n' +
    'Sub O()\r\n' +
    'End Sub\r\n'
)


worst_expected = """\
%s:1:1: E505 optional public
%s:1:1: E601 missing module attributes
%s:1:51: E131 Excess whitespace before '('
%s:1:53: E134 Excess whitespace after '('
%s:1:63: E151 Excess whitespace before ','
%s:1:66: E154 Excess whitespace after ','
%s:1:80: W501 line too long (92 > 79 characters)
%s:1:90: E141 Excess whitespace before ')'
%s:1:92: E144 Excess whitespace after ')'
%s:1:92: E305 trailing whitespace
%s:1:92: E500 incorrect line ending
%s:2:0: E500 incorrect line ending
%s:4:0: W303 Too many blank lines (3)
%s:5:1: W110 Missing let
%s:5:11: E500 incorrect line ending
%s:6:5: W110 Missing let
%s:6:12: E160 Missing whitespace before '='
%s:6:13: E163 Missing whitespace after '='
%s:7:5: W111 Optional let
%s:7:16: E161 Excess whitespace before '='
%s:7:19: E164 Excess whitespace after '='
%s:8:12: E500 incorrect line ending
%s:10:1: W510 Missing visibility
%s:12:1: W391 blank line at end of file
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
    full_path = ("/home/runner/work/VBA-Linter/VBA-Linter/" + file_name)
    expected = """\
%s:1:1: E601 missing module attributes
%s:1:51: E131 Excess whitespace before '('
%s:1:53: E134 Excess whitespace after '('
%s:1:63: E151 Excess whitespace before ','
%s:1:66: E154 Excess whitespace after ','
%s:1:90: E141 Excess whitespace before ')'
%s:1:92: E144 Excess whitespace after ')'
%s:1:92: E305 trailing whitespace
%s:1:92: E500 incorrect line ending
%s:2:0: E500 incorrect line ending
%s:5:11: E500 incorrect line ending
%s:6:12: E160 Missing whitespace before '='
%s:6:13: E163 Missing whitespace after '='
%s:7:16: E161 Excess whitespace before '='
%s:7:19: E164 Excess whitespace after '='
%s:8:12: E500 incorrect line ending
16 Errors in 1 File
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
    delete_code(file_name)


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
        'Private Sub Open()\r\n' +
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
