from behave.__main__ import main as behave_main


def test_behave_features():
    exit_code = behave_main(["features"])
    assert exit_code == 0, "Behave scenarios failed."
