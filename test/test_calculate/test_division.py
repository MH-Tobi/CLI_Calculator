from click.testing import CliRunner
import test.test_helper_functions as helper_functions


# Test Division
def test_division_two_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "10/2", '5.0\n')

def test_division_three_positive_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "30/5/2", '3.0\n')

def test_division_two_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-30/-3", '10.0\n')

def test_division_three_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-180/-5/-2", '-18.0\n')

def test_division_positive_and_negative_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "180/-18/-5/2", '1.0\n')

def test_division_two_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.15/4.35", '0.0344827586\n')

def test_division_three_positive_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0.23/3.45/5.01", '0.0133067199\n')

def test_division_two_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-1.2/-2.03", '0.5911330049\n')

def test_division_three_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.7/-3.73/-6.15", '-0.1177009089\n')

def test_division_positive_and_negative_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2.01/3.645/6.78/-1.545/-0.01", '-5.2642965625\n')