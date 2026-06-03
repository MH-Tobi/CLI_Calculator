from click.testing import CliRunner
import test.test_helper_functions as helper_functions
from calculator import calculator


# Test Addition
def test_with_empty_history():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    result = runner.invoke(calculator.menu, ['--clean-history'])
    assert result.exit_code == 0
    assert result.output == "History cleared successfully.\n"

def test_with_filled_history():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)
    result = runner.invoke(calculator.menu, ['--clean-history'])
    assert result.exit_code == 0
    assert result.output == 'History cleared successfully.\n'