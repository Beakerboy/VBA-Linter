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
    main()
    captured = capsys.readouterr()
    assert captured.err == "foo"


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
    assert captured.err == "foo"
