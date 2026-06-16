from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


def test_empty_last_result_at_beginning():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    # res = 0
    helper_functions._calculate_test_helper(runner, "res-2", '-2\n')

def test_empty_last_result_at_the_end():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    # res = 0
    helper_functions._calculate_test_helper(runner, "2-res", '2\n')

def test_empty_last_result_between():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    # res = 0
    helper_functions._calculate_test_helper(runner, "2-res+5", '7\n')

def test_defined_last_result_at_beginning():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "res-2", '13\n')

def test_defined_last_result_at_the_end():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "2-res", '-13\n')

def test_defined_last_result_between():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "2-res+5", '-8\n')

def test_multiple_last_results():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "2-res*-res+12", '239\n')