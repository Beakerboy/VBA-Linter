from pytest_mock import MockerFixture
from vba_linter.__main__ import main


def test_form(mocker: MockerFixture) -> None:
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            "tests/files",
            "all"
        ],
    )
    main()
