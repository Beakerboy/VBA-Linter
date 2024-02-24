from pytest_mock import MockerFixture
from vba_linter.__main__ import main


def test_form(mocker: MockerFixture, capsys: CaptureFixture) -> None:
    file_name = save_code(worst_practice)
    files.append(file_name)
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "tests/files",
            "all"
        ],
    )
    main()
