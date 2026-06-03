from click.testing import CliRunner
import test.test_helper_functions as helper_functions


# Test combinations of multiple types
def test_combination_integer_1():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-2+10*2/5-15+-8--9", '-12.0\n')

def test_combination_integer_2():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "7*-4--15*2+3/-5/6", '1.9\n')

def test_combination_floats_1():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "-0.2+-10.236*2.645/-0.565-1.655", '46.0639734513\n')

def test_combination_floats_2():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1.54*-6.68/-46.65+45.977*1235.201354", '56791.0731716147\n')
