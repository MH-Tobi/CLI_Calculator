from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


# Test Substraction
def test_substraction_two_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "10-3", '7\n')

def test_substraction_three_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "10-2-5", '3\n')

def test_substraction_two_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-12--1", '-11\n')

def test_substraction_three_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-1--12--3", '14\n')

def test_substraction_positive_and_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "2-3-6--15--1", '9\n')

def test_substraction_two_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.15-4.35", '-4.2\n')

def test_substraction_three_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.23-3.45-5.01", '-8.23\n')

def test_substraction_two_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-1.2--2.03", '0.83\n')

def test_substraction_three_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.7--3.73--6.15", '7.18\n')

def test_substraction_positive_and_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.01-3.645-6.78--1.545--0.01", '-10.88\n')
