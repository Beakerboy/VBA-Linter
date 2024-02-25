import pytest
import random
import string
from pathlib import Path
from pytest_mock import MockerFixture
from _pytest.capture import CaptureFixture
from vba_linter.__main__ import main


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


worst_practice1 = (
    'Attribute VB_Name = "Foo"\r\n' +
    '\r\n'
    'Public Function ' + function +
    ' ( atrocious ,  precocious, indubitably ) \r\n' +
    ' \r\n' +
    '\r\n' +
    ' \' noqa: 400\n' +
    '\r\n' +
    'I = (2 + 1)\r\n' +
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
%s:11:12: E400 incorrect line ending
%s:13:1: E220 Keyword not capitalized
12 Errors in 1 File
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
