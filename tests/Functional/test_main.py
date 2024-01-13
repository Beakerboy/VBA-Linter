import pytest
import random
import string
from pathlib import Path
from pytest_mock import MockerFixture
from _pytest.capture import CaptureFixture
from vba_linter.__main__ import main


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
file_name = save_code(worst_practice)


def test_worst_file(mocker: MockerFixture, capsys: CaptureFixture) -> None:
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
    captured = capsys.readouterr()
    full_path = ("/home/runner/work/VBA-Linter/VBA-Linter/" + file_name)
    expected = """\
%s:1:1: N104 missing module attributes
%s:1:1: Wxxx optional public
%s:1:51: E211 whitespace before '('
%s:1:53: E201 Whitespace after '('
%s:1:63: E203 Whitespace before ','
%s:1:80: W501 line too long (92 > 79 characters)
%s:1:90: E202 Whitespace before ')'
%s:1:92: W291 trailing whitespace
%s:1:92: W500 incorrect line ending
%s:2:0: W500 incorrect line ending
%s:4:0: E303 Too many blank lines (3)
%s:5:1: Wxxx missing let
%s:5:11: W500 incorrect line ending
%s:6:5: Wxxx missing let
%s:6:12: R225 missing space before '='
%s:6:13: R225 missing space after '='
%s:7:5: Wxxx optional let
%s:7:16: W221 multiple spaces before operator
%s:7:19: W222 multiple spaces after operator
%s:8:12: W500 incorrect line ending
%s:10:1: Wxxx missing visibility
%s:12:1: W391 blank line at end of file
22 Errors in 1 File
""".replace("%s", full_path)  # noqa
    assert captured.err == expected
    f = open(file_name + ".pretty", "r", newline='')
    pretty_file = f.read()
    assert pretty_file == pretty
    delete_code(file_name + ".pretty")

    expected = """\
%s:1:1: N104 missing module attributes
%s:1:51: E211 whitespace before '('
%s:1:53: E201 Whitespace after '('
%s:1:63: E203 Whitespace before ','
%s:1:80: W501 line too long (92 > 79 characters)
%s:1:90: E202 Whitespace before ')'
%s:1:92: W291 trailing whitespace
%s:1:92: W500 incorrect line ending
%s:2:0: W500 incorrect line ending
%s:4:0: E303 Too many blank lines (3)
%s:5:11: W500 incorrect line ending
%s:6:12: R225 missing space before '='
%s:6:13: R225 missing space after '='
%s:7:5: Wxxx optional let
%s:7:16: W221 multiple spaces before operator
%s:7:19: W222 multiple spaces after operator
%s:8:12: W500 incorrect line ending
%s:10:1: Wxxx missing visibility
%s:12:1: W391 blank line at end of file
19 Errors in 1 File
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


def test_worst_zero(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    """
    Ensure that --exit-zero returns the same output, but does not trigger
    an exception
    """
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
    expected = """\
%s:1:1: N104 missing module attributes
%s:1:1: Wxxx optional public
%s:1:51: E211 whitespace before '('
%s:1:53: E201 Whitespace after '('
%s:1:63: E203 Whitespace before ','
%s:1:80: W501 line too long (92 > 79 characters)
%s:1:90: E202 Whitespace before ')'
%s:1:92: W291 trailing whitespace
%s:1:92: W500 incorrect line ending
%s:2:0: W500 incorrect line ending
%s:4:0: E303 Too many blank lines (3)
%s:5:1: Wxxx missing let
%s:5:11: W500 incorrect line ending
%s:6:5: Wxxx missing let
%s:6:12: R225 missing space before '='
%s:6:13: R225 missing space after '='
%s:7:5: Wxxx optional let
%s:7:16: W221 multiple spaces before operator
%s:7:19: W222 multiple spaces after operator
%s:8:12: W500 incorrect line ending
%s:10:1: Wxxx missing visibility
%s:12:1: W391 blank line at end of file
22 Errors in 1 File
""".replace("%s", full_path)  # noqa
    assert captured.err == expected


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
