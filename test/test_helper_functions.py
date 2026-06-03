from src.calculator import calculator


def _calculate_test_helper(runner, operation, expected_result):
    result = runner.invoke(calculator.calculate, ['--', operation])
    assert result.exit_code == 0
    assert result.output == expected_result

def _clear_calculator(runner):
    runner.invoke(calculator.menu, ['--clean-history'])
    runner.invoke(calculator.menu, ['--clean-variables'])

def _fill_history(runner):
    runner.invoke(calculator.calculate, ['--', "1+2"])
    runner.invoke(calculator.calculate, ['--', "5*7"])
    runner.invoke(calculator.calculate, ['--', "-11+0.2"])
    runner.invoke(calculator.calculate, ['--', "-1.1+2"])
    runner.invoke(calculator.calculate, ['--', "4+5+6"])

def _fill_variables(runner):
    runner.invoke(calculator.menu, ['--set-variable', "a", "15"])
    runner.invoke(calculator.menu, ['--set-variable', "ab", "-5"])
    runner.invoke(calculator.menu, ['--set-variable', "abc", "3"])
    runner.invoke(calculator.menu, ['--set-variable', "abcd", "-0.22"])
    runner.invoke(calculator.menu, ['--set-variable', "abcde", "3.14159"])
