from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


# Test Modulo
def test_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "10%2", '0\n')

def test_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-4%-3", '-1\n')

def test_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1.067%2.78", '1.067\n')

def test_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-33.224%-2.97", '-0.554\n')

def test_zero():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0%34", '0\n')

def test_multiple_modulos():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "(34.92%2.1)%(43.21*0.12)", '1.32\n')