from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


# Test Exponential
def test_positive_integer():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "4^2", '16\n')

def test_negative_integer():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "4^-2", '0.0625\n')

def test_positive_float():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "3.68^2.98", '48.554166097\n')

def test_negative_float():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "3.68^-2.98", '0.020595555\n')

def test_alternative_operator_positive_integer():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "9**3", '729\n')

def test_alternative_operator_negative_integer():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "9**-3", '0.0013717421\n')

def test_alternative_operator_positive_float():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "35.68**0.12", '1.5356455355\n')

def test_alternative_operator_negative_float():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "35.68**-0.12", '0.651191943\n')

def test_zero_power_zero():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "0^0", '1\n')

def test_squareroot_2():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "2**0.5", '1.4142135624\n')