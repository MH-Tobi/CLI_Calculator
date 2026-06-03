from click.testing import CliRunner
import test.test_helper_functions as helper_functions
from calculator import calculator


def test_with_allowed_variable_name_and_value_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    result = runner.invoke(calculator.menu, ['--set-variable', "ab", "-323.98"])
    assert result.exit_code == 0
    assert result.output == "Variable \"ab\" has been set with value \"-323.98\".\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'ab = -323.98\n\n'

def test_with_allowed_variable_name_and_value_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    result = runner.invoke(calculator.menu, ['--set-variable', "cd", "0.23"])
    assert result.exit_code == 0
    assert result.output == "Variable \"cd\" has been set with value \"0.23\".\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'cd = 0.23\n\n'

def test_with_res_as_unallowed_variable_name():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    result = runner.invoke(calculator.menu, ['--set-variable', "res", "1.2"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Name \"res\" is reserved.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_res_as_allowed_variable_value():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    result = runner.invoke(calculator.menu, ['--set-variable', "ad", "res"])
    assert result.exit_code == 0
    assert result.output == "Variable \"ad\" has been set with value \"15\".\n"

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "ad = 15\n\n"

def test_with_already_used_variable_name():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "ab", "1.2"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Name \"ab\" already exists.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == 'a = 15\nab = -5\nabc = 3\nabcd = -0.22\nabcde = 3.14159\n\n'

def test_with_constants_name_as_variable_name_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "cahen", "1.2"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Name \"cahen\" must not be a constant.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_constants_name_as_variable_name_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "gaus_kusmin_wirsing", "1.2"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Name \"gaus_kusmin_wirsing\" must not be a constant.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_numeric_variable_name_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "432", "1.2"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Name \"432\" must not be numeric.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_numeric_variable_name_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "0.54", "1.2"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Name \"0.54\" must not be numeric.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_numeric_variable_name_3():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "-50.89", "1.2"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Name \"-50.89\" must not be numeric.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_non_numeric_variable_value_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "ef", "NAN"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Value \"NAN\" has to be numeric.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_non_numeric_variable_value_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "ef", "t329"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Value \"t329\" has to be numeric.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_non_numeric_variable_value_3():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "ef", "22g"])
    assert result.exit_code == 0
    assert result.output == 'Variable-Value \"22g\" has to be numeric.\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_whitespaces_in_variable_name_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "e f", "-23.45"])
    assert result.exit_code == 0
    assert result.output == 'Whitespace are not allowed in the Variable-Name \"e f\".\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_whitespaces_in_variable_name_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "e\tf", "-23.45"])
    assert result.exit_code == 0
    assert result.output == 'Whitespace are not allowed in the Variable-Name \"e\tf\".\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"

def test_with_whitespaces_in_variable_name_3():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    result = runner.invoke(calculator.menu, ['--set-variable', "e\nf", "-23.45"])
    assert result.exit_code == 0
    assert result.output == 'Whitespace are not allowed in the Variable-Name \"e\nf\".\n'

    result = runner.invoke(calculator.menu, ['--get-variables'])
    assert result.exit_code == 0
    assert result.output == "\n"