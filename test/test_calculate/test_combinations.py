from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


# Test combinations of multiple types
def test_basic_arithmetic_with_integers():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2+10*2/5-15+-8--9", '-12.0\n')

def test_basic_arithmetic_with_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-0.2+-10.236*2.645/-0.565-1.655", '46.0639734513\n')

def test_basic_arithmetic_with_integers_and_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "22*15.875-54.87/-65-66+-88.565", '195.5291538462\n')

def test_parenthesis_pairs_and_exponential():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "(2.43*3.6**(2-(4/2)))^(20*0.1)", '5.9049\n')

def test_modulo_with_parenthesis_pairs():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "(2.43*3.6**(2-(4/2)))%(20*0.1)", '0.43\n')