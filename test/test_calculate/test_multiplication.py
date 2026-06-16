from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


# Test Multiplication
def test_two_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1*3", '3\n')

def test_three_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1*3*5", '15\n')

def test_two_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2*-6", '12\n')

def test_three_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-5*-2*-3", '-30\n')

def test_positive_and_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "2*3*-6*-15*-2", '-1080\n')

def test_two_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.15*4.35", '0.6525\n')

def test_three_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.23*3.45*5.01", '3.975435\n')

def test_two_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-1.2*-2.03", '2.436\n')

def test_three_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.7*-3.73*-6.15", '-61.93665\n')

def test_positive_and_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.01*3.645*6.78*-1.545*-0.01", '-0.7674529639\n')
