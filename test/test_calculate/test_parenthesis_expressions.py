from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


def test_positive_integer_in_parenthesis():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "2+(3)+4", '9\n')

def test_negative_integer_in_parenthesis():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "2+(-3)+4", '3\n')

def test_positive_float_in_parenthesis():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "(2.354)*35-2", '80.39\n')

def test_negative_float_in_parenthesis():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "(-2.354)*35-2", '-84.39\n')

def test_expression_in_parenthesis():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-265*(98/103.87-3)-56", '488.9759314528\n')

def test_multiple_parenthesis_pairs():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "98.24*(32-51)/(23+1.3-(65.7*(13-2.35))-2)", '2.7554564847\n')
