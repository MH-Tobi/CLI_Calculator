from click.testing import CliRunner
import test.test_helper_functions as helper_functions

# Variables
# a     = 15
# ab    = -5
# abc   = 3
# abcd  = -0.22
# abcde = 3.14159

def test_variables_replacement_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    helper_functions._calculate_test_helper(runner, "ab+abcde+a-abc-abcd", '10.36159\n')

def test_variables_replacement_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    helper_functions._calculate_test_helper(runner, "a+ab+abc+abcd+abcde", '15.92159\n')

def test_variables_replacement_3():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    helper_functions._calculate_test_helper(runner, "abcde+abcd+abc+ab+a", '15.92159\n')

def test_variables_replacement_4():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)
    helper_functions._fill_variables(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "15.345-54.34*-res/abcd+ab*-2", '-3679.655\n')