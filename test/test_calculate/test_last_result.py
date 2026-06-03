from click.testing import CliRunner
import test.test_helper_functions as helper_functions


def test_with_empty_last_result_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    # res = 0
    helper_functions._calculate_test_helper(runner, "res-2", '-2\n')

def test_with_empty_last_result_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)

    # res = 0
    helper_functions._calculate_test_helper(runner, "2-res", '2\n')

def test_with_last_result_1():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "res-2", '13\n')

def test_with_last_result_2():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "2-res", '-13\n')

def test_with_last_result_3():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    helper_functions._fill_history(runner)

    # res = 15
    helper_functions._calculate_test_helper(runner, "2-res*-res+12", '239\n')