import pytest
from pytest_mock import MockerFixture
from vba_linter.__main__ import main


def test_bad_file(mocker: MockerFixture) -> None:
    dir_path = "tests/Files"
    mocker.patch(
        "sys.argv",
        [
            "vba_linter.py",
            dir_path
        ],
    )
    main()
