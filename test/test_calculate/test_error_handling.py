from click.testing import CliRunner
from test.helper_functions import test_helper_functions as helper_functions


def test_unexpected_character_minus():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15---2", "The character \"-\" in the substring \"--2\" is not expected.\n")

def test_unexpected_character_point():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15..68-2", "The character \".\" in the substring \".68-2\" is not expected.\n")

def test_missing_operator_between_two_floats():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "32-44.23*9.32 0.65-4", "The character \".\" in the substring \".65-4\" is not expected.\n")

def test_unexpected_character_letter_h():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+Here_Error-2", "The character \"H\" in the substring \"Here_Error-2\" is not expected.\n")

def test_unexpected_character_letter_backslash():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+-2*4\\5", "The character \"\\\" in the substring \"\\5\" is not expected.\n")

def test_unexpected_character_letter_e():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+-2*4E45", "The character \"E\" in the substring \"E45\" is not expected.\n")

def test_division_by_zero_by_direct_zero():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+-2*4/0", "Division by zero error.\n")

def test_division_by_zero_by_calculated_zero():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15/(32-32)+-2", "Division by zero error.\n")

def test_whitespaces_around_operator():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1 + 3", '4\n')

def test_multiple_whitespaces_around_operator():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1   + 3", '4\n')

def test_tabulator():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "1\t+3", '4\n')

def test_whitespaces_in_front_of_operation():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "   1+3", '4\n')

def test_new_line():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "\n1+3", '4\n')

def test_multiple_new_lines():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "\n1\n+\n3\n", '4\n')

def test_missing_opening_parenthesis():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "21*(65-98)+6.23)*2", 'Missing opening parenthesis.\n')

def test_missing_closing_parenthesis():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "654.8874/0.21*(98+36*(68)", 'Missing closing parenthesis.\n')

def test_missing_operator_before_parenthesis_pairs():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "3.24/(322.1-1.56(0.027))", "An operator is missing in the expression \"3.24/(322.1-1.56(0.027))\".\n")

def test_missing_operator_after_parenthesis_pairs():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "(32.15*64)0.335-2", "An operator is missing in the expression \"(32.15*64)0.335-2\".\n")

def test_missing_operator_between_two_parenthesis_pairs():
    runner = CliRunner()
    helper_functions._calculate_test_helper(runner, "15+((-2)*4)(45+5)", "An operator is missing in the expression \"15+((-2)*4)(45+5)\".\n")