from __main__ import main


def test_line_ending() -> None:
    assert main("\n") == "fail"
    assert main("\r\n") == ""
    assert main("\r") == "fail"
    assert main("\r \n") == "fail"
