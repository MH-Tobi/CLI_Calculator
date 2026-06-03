from click.testing import CliRunner
import test.test_helper_functions as helper_functions
from src.calculator import calculator


# Test Addition
def test_with_empty_history():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    result = runner.invoke(calculator.menu, ['--get-history'])
    assert result.exit_code == 0
    assert result.output == "No history created.\n"

def test_with_filled_history():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)
    result = runner.invoke(calculator.menu, ['--get-history'])
    assert result.exit_code == 0
    assert result.output == '1+2\t3\n5*7\t35\n-11+0.2\t-10.8\n-1.1+2\t0.9\n4+5+6\t15\n\n'