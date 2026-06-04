from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions
import calculator


def test_with_empty_variables():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == '\n'

    result = runner.invoke(calculator.menu, ['--clean-variables'])
    assert result.exit_code == 0
    assert result.output == "Variables cleared successfully.\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == '\n'

def test_with_filled_variables():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'a = 15\nab = -5\nabc = 3\nabcd = -0.22\nabcde = 3.14159\n\n'

    result = runner.invoke(calculator.menu, ['--clean-variables'])
    assert result.exit_code == 0
    assert result.output == "Variables cleared successfully.\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == '\n'