from click.testing import CliRunner
import test.test_helper_functions as helper_functions


def test_syntax_error_1():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15---2", "Substring \"--2\" contains an error.\n")

def test_syntax_error_2():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15**-2", "Substring \"*-2\" contains an error.\n")

def test_syntax_error_3():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15*(-2)", "Substring \"(-2)\" contains an error.\n")

def test_syntax_error_4():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+Here_Error-2", "Substring \"Here_Error-2\" contains an error.\n")

def test_unknown_operator_1():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+-2*4^5", "Unknown Operator \"^\".\n")

def test_unknown_operator_2():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+-2*4\\5", "Unknown Operator \"\\\".\n")

def test_unknown_operator_3():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+-2*4E45", "Unknown Operator \"E\".\n")

def test_division_by_zero_1():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+-2*4/0", "Division by zero error.\n")

def test_division_by_zero_2():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15/0+-2", "Division by zero error.\n")

def test_whitespaces_1():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1 + 3", '4\n')

def test_whitespaces_2():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1   + 3", '4\n')

def test_whitespaces_3():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1\t+3", '4\n')

def test_whitespaces_4():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "   1+3", '4\n')

def test_whitespaces_5():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "\n1+3", '4\n')

def test_whitespaces_6():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "\n1\n+\n3\n", '4\n')