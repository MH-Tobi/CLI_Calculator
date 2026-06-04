from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


# Test Addition
def test_addition_two_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1+3", '4\n')

def test_addition_three_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1+3+5", '9\n')

def test_addition_two_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-1+-2", '-3\n')

def test_addition_three_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2+-3+-6", '-11\n')

def test_addition_positive_and_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2+3+6+-15+-1", '-9\n')

def test_addition_two_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.1+3.7", '3.8\n')

def test_addition_three_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.23+3.45+5.01", '8.69\n')

def test_addition_two_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-1.2+-2.03", '-3.23\n')

def test_addition_three_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.7+-3.73+-6.15", '-12.58\n')

def test_addition_positive_and_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.01+3.645+6.78+-1.545+-0.01", '6.86\n')
