from click.testing import CliRunner
import test.test_helper_functions as helper_functions
from src.calculator import calculator


def test_with_unknown_variable_name():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    result = runner.invoke(calculator.menu, ['--delete-variable', "unknown"])
    assert result.exit_code == 0
    assert result.output == "Variable \"unknown\" does not exist.\n\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'a = 15\nab = -5\nabc = 3\nabcd = -0.22\nabcde = 3.14159\n\n'

def test_with_known_variable_name():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    result = runner.invoke(calculator.menu, ['--delete-variable', "ab"])
    assert result.exit_code == 0
    assert result.output == "Variable \"ab\" with value \"-5\" has been deleted.\n\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'a = 15\nabc = 3\nabcd = -0.22\nabcde = 3.14159\n\n'

def test_with_multiple_variable_names():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    result = runner.invoke(calculator.menu, ['--delete-variable', "ab", '--delete-variable', "abc", '--delete-variable', "abcde"])
    assert result.exit_code == 0
    assert result.output == "Variable \"ab\" with value \"-5\" has been deleted.\nVariable \"abc\" with value \"3\" has been deleted.\nVariable \"abcde\" with value \"3.14159\" has been deleted.\n\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'a = 15\nabcd = -0.22\n\n'

def test_with_multiple_known_and_unknown_variable_names():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    result = runner.invoke(calculator.menu, ['--delete-variable', "ab", '--delete-variable', "unknown", '--delete-variable', "abcde"])
    assert result.exit_code == 0
    assert result.output == "Variable \"ab\" with value \"-5\" has been deleted.\nVariable \"unknown\" does not exist.\nVariable \"abcde\" with value \"3.14159\" has been deleted.\n\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'a = 15\nabc = 3\nabcd = -0.22\n\n'