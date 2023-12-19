from pytest_mock import MockerFixture
from _pytest.capture import CaptureFixture
from vba_linter.__main__ import main


def test_bad_file(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    dir_path = "tests/Files/project"
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            dir_path
        ],
    )
    with mocker.patch.object(main.sys, "exit") as mock_exit:
        main()
        assert mock_exit.call_args[0][0] == 1
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
    main()
    captured = capsys.readouterr()
    assert captured.err == (
        "/home/runner/work/VBA-Linter/VBA-Linter/tests/Files/Fail/fail.bas" +
        ":3:14: E999 extraneous input '+1' expecting {',', ')', WS}\n"
    )
