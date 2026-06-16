from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions

# Variables
# a     = 15
# ab    = -5
# abc   = 3
# abcd  = -0.22
# abcde = 3.14159

def test_replace_variables_random_order():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    helper_functions._calculate_test_helper(runner, "ab+abcde+a-abc-abcd", '10.36159\n')

def test_replace_variables_ascending_order_by_length():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    helper_functions._calculate_test_helper(runner, "a+ab+abc+abcd+abcde", '15.92159\n')

def test_replace_variables_descending_order_by_length():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_variables(runner)
    helper_functions._calculate_test_helper(runner, "abcde+abcd+abc+ab+a", '15.92159\n')

def test_replace_variables_and_constants():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)
    helper_functions._fill_variables(runner)

    # lemniskat = 2.62205755429211981046
    # chintschin_levy = 1.18656911041562545282
    helper_functions._calculate_test_helper(runner, "15.345/chintschin_levy-54.34*lemniskat/abcd+ab*-2", '670.5804588493\n')