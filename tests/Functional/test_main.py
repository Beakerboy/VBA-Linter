import pytest
import random
import string
from pathlib import Path
from pytest_mock import MockerFixture
from _pytest.capture import CaptureFixture
from vba_linter.__main__ import main


def test_worst_file(mocker: MockerFixture, capsys: CaptureFixture) -> None:
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
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "-x",
            "tests/Functional"
        ],
    )
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    full_path = ("/home/runner/work/VBA-Linter/VBA-Linter/" + file_name)
    expected = """\
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
%s:6:12: R225 missing space before '='
%s:6:13: R225 missing space after '='
%s:6:5: Wxxx missing let
%s:7:5: Wxxx optional let
%s:8:12: W500 incorrect line ending
%s:10:1: Wxxx missing visibility
%s:12:1: W391 blank line at end of file
19 Errors in 1 File
""".replace("%s", full_path)  # noqa
    assert captured.err == expected
    delete_code(file_name)
    f = open(file_name + ".pretty", "r", newline='')
    pretty_file = f.read()
    assert pretty_file == pretty
    delete_code(file_name + ".pretty")


def test_bad_file(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    dir_path = "tests/Files/project"
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            dir_path
        ],
    )
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    expected = """\
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:1:51: E211 whitespace before '('
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:1:53: E201 Whitespace after '('
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:1:63: E203 Whitespace before ','
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:1:80: W501 line too long (91 > 79 characters)
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:1:89: E202 Whitespace before ')'
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:1:91: W291 trailing whitespace
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:1:91: W500 incorrect line ending
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:2:0: W500 incorrect line ending
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:3:13: W500 incorrect line ending
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/project/all_errors.bas:4:12: W500 incorrect line ending
10 Errors in 1 File
"""  # noqa
    assert captured.err == expected


def test_fail_file(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    dir_path = "tests/Files/Fail"
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            dir_path
        ],
    )
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    expected = """\
/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/Fail/fail.bas:3:14: E999 extraneous input '+1' expecting {',', ')', WS}
1 Error in 1 File
"""  # noqa
    assert captured.err == expected


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
