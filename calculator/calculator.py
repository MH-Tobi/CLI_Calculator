import click
import re
import os
import json
import copy

# https://de.wikipedia.org/wiki/Mathematische_Konstante
constants = {
    "pi":                       "3.14159265358979323846",
    "squareroot_2":             "1.41421356237309504880",
    "squareroot_3":             "1.73205080756887729352",
    "golden_ratio":             "1.61803398874989484820",
    "euler":                    "2.71828182845904523536",
    "euler_mascheroni":         "0.57721566490153286060",
    "apery":                    "1.20205690315959428539",
    "erdos_borwein":            "1.60669515241529176378",
    "ramanujan_soldner":        "1.45136923488338105028",
    "lemniskat":                "2.62205755429211981046",
    "legendre":                 "1.08366",
    "laplace_limit":            "0.66274341934918158097",
    "catalan":                  "0.91596559417721901505",
    "meissel_mertens":          "0.26149721284764278375",
    "glaisher_kinkelin":        "1.28242712910062263687",
    "cahen":                    "1.73205080756887729352",
    "sierpinski":               "2.58498175957925321706",
    "landau_ramanujan":         "0.76422365358922066299",
    "gieseking":                "1.01494160640965362502",
    "bernstein":                "0.28016949902386913303",
    "brun":                     "1.90216058",
    "twin_prime":               "0.66016181584686957392",
    "golomb_dickman":           "0.62432998854355087099",
    "chintschin":               "2.68545200106530644530",
    "chintschin_levy":          "1.18656911041562545282",
    "mills":                    "1.30637788386308069046",
    "liebs":                    "1.53960071783900203869",
    "niven":                    "1.70521114010536776428",
    "gaus_kusmin_wirsing":      "0.30366300289873265859",
    "porter":                   "1.46707807943397547289",
    "chaitin":                  "0.0078749969978123844",
    "alladi_grinstead":         "0.80939402054063913071",
    "feigenbaum_1":             "4.66920160910299067185",
    "feigenbaum_2":             "2.50290787509589282228",
    "fransen_robinson":         "2.80777024202851936522",
    "lengyel":                  "1.09868580552518701",
    "hafner_sarnak_mccurley":   "0.35323637185499598454",
    "backhouse":                "1.45607494858268967139",
    "viswanath":                "1.1319882487943",
    "embree_trefethen":         "0.70258"
}

def _prepare_string(string):

    # Collect Values for the last Result, Variables and Constants
    result_last_result, value_last_result = _get_last_result()
    result_variables, value_variables = _get_variables()
    result_constants, value_constants = _get_constants()

    # Return in case of an Error during the Collection
    if not result_last_result:
        return False, value_last_result
    if not result_variables:
        return False, value_variables
    if not result_constants:
        return False, value_constants

    # Create lists from collected Values and concatenate them
    variable_list = list(value_variables.items())
    constant_list = list(value_constants.items())
    blocked_variable_names = variable_list + constant_list + [("res", value_last_result)]

    # Sort list by length of Value-Names
    blocked_variable_names.sort(key=lambda x: len(x[0]), reverse=True)

    # Remove all Whitespaces from the String
    string = "".join(string.split())

    # Replace Value-Names in the String with the actual Value
    for name, value in blocked_variable_names:
        if name in string:
            string = string.replace(name, value)

    return True, string


def _write_history(operation, result):
    try:
        # Try to append operation and the result of the operation to the file "calculator_history"
        with open(os.path.join(os.path.dirname(__file__), 'calculator_history'), "a") as f:
            f.write(f"{operation}\t{result}\n")
    except OSError:
        # In case of an OSError return the Error-Message
        return False, f"File \"calculator_history\" cannot be opened to write."
    else:
        return True, f"History written successfully."


def _get_constants():
    # Return the Dictionary of the Constants
    return True, constants


def _get_history():
    history = []
    if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_history')):
        try:
            # Try to read the calculator-history from the file "calculator_history"
            with open(os.path.join(os.path.dirname(__file__), 'calculator_history'), "r") as f:
                for line in f.readlines():
                    history.append(line)
        except OSError:
            # In case of an OSError return the Error-Message
            return False, f"File \"calculator_history\" cannot be opened for read."

    return True, history


def _get_variables():
    variables = {}
    try:
        # Try to read the calculator-variables from the file "calculator_variables"
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_variables')):
            with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "r") as f:
                variables = json.load(f)
    except OSError:
        # In case of an OSError return the Error-Message
        return False, f"File \"calculator_variables\" cannot be opened for read."
    else:
        return True, variables


def _set_variables(name, value):
    # Check if the Value of the new Variable should be the last Result
    if value == "res":
        result, value = _get_last_result()
        if not result:
            return False, value

    # Collect the Variables
    result, variables = _get_variables()

    if result:
        # Do some Checks
        if name in variables.keys():
            return False, f"Variable-Name \"{name}\" already exists."
        elif name in constants.keys():
            return False, f"Variable-Name \"{name}\" must not be a constant."
        elif re.search(r'^[+\-]?[0-9]+\.?[0-9]*$', name):
            return False, f"Variable-Name \"{name}\" must not be numeric."
        elif not re.search(r'^[+\-]?[0-9]+\.?[0-9]*$', value):
            return False, f"Variable-Value \"{value}\" has to be numeric."
        elif name == "res":
            return False, f"Variable-Name \"res\" is reserved."
        elif len(name.split()) != 1:
            return False, f"Whitespace are not allowed in the Variable-Name \"{name}\"."
        else:
            variables[name] = value
            try:
                # Try to write variables to the file "calculator_variables"
                with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "w") as f:
                    json.dump(variables, f)
            except OSError:
                # In case of an OSError return the Error-Message
                return False, f"File \"calculator_variables\" cannot be opened to write."
            else:
                return True, f"Variable \"{name}\" has been set with value \"{value}\"."
    else:
        return False, variables


def _delete_variable(names):
    # Collect all variables
    result, variables = _get_variables()

    message = ""

    if result:
        # For each Variable to delete
        for name in names:
            # Check if Variable exists
            if not name in variables.keys():
                message += f"Variable \"{name}\" does not exist.\n"
            else:
                # Remove Variable from Dictionary
                value = variables[name]
                variables.pop(name)
                try:
                    # Try to write variables to the file "calculator_variables"
                    with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "w") as f:
                        json.dump(variables, f)
                except OSError:
                    # In case of an OSError return the Error-Message
                    return False, f"File \"calculator_variables\" cannot be opened to write."
                else:
                    message += f"Variable \"{name}\" with value \"{value}\" has been deleted.\n"

        return True, message
    else:
        return False, variables


def _clean_variables():
    variables = {}
    try:
        # Try to delete all variables by writing an empty Dictionary to the file "calculator_variables"
        with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "w") as f:
            json.dump(variables, f)
    except OSError:
        # In case of an OSError return the Error-Message
        return False, f"File \"calculator_variables\" cannot be opened to write."
    else:
        return True, f"Variables cleared successfully."


def _clear_history():
    try:
        # Try to delete history by writing an empty string to the file "calculator_history"
        with open(os.path.join(os.path.dirname(__file__), 'calculator_history'), "w") as f:
            f.write("")
    except OSError:
        # In case of an OSError return the Error-Message
        return False, f"File \"calculator_variables\" cannot be opened to write."
    else:
        return True, f"History cleared successfully."


def _get_last_result():
    last_result = "0"

    # Collect the history
    result, history = _get_history()

    if result:
        if history:
            # Getting the last Result from the last entry of the history
            last_result = history[-1].split("\t")[-1].strip("\n")

        return True, last_result
    else:
        return False, history


def _change_type_to_numeric(string_numbers):
    numeric_numbers = []

    # Change type of the Number from string to Int or Float
    for string_number in string_numbers:
        if type(string_number) == list:
            # If current entry is a list, change the types for this list
            result, values = _change_type_to_numeric(string_number)
            if result:
                numeric_numbers.append(values)
            else:
                return result, values
        else:
            try:
                if "." in string_number:
                    numeric_numbers.append(float(string_number))
                else:
                    numeric_numbers.append(int(string_number))
            except BaseException:
                return False, "Something went wrong while changing the type to numeric."

    return True, numeric_numbers


def _result_output_handler(operation, value):
    if type(value) == float:
        value = round(value, 10)
        click.echo(value, err=False)
        result, message = _write_history(operation, value)
    elif type(value) == int:
        click.echo(value, err=False)
        result, message = _write_history(operation, value)
    else:
        result = False
        message = f"Unknown Type of the result {type(value)}."

    return result, message


def _analyse_string(string, level):

    numbers = []
    operators = []
    string_analysed = False

    # Start analysis
    while not string_analysed:

        # Search for the given pattern from the beginning of the String
        match = re.search(r'^[+\-]?[0-9]+\.?[0-9]*', string)
        if match:
            # when there is a match, the matched number is added to the numbers-List
            numbers.append(string[:match.regs[0][1]])

            # and the number is removed from the string
            string = string[match.regs[0][1]:]

            if len(string) > 0:
                ## as long there are characters after the matched number,
                ## the next character is checked if it is an operator or a closing parenthesis
                if string[0] in ["+", "-", "*", "/"]:
                    # In case of an operator it is added to the operators-list
                    operators.append(string[0])

                    # and the operator is removed from the string
                    string = string[1:]
                elif string[0] == ")":
                    # In case of a closing parenthesis it is checked if we are in a greater level than 0
                    if level > 0:
                        # In this case we can return the string without the closing parenthesis and the collected numbers and operators
                        return string[1:], numbers, operators
                    else:
                        # If we are in level 0 there has to be a missing opening parenthesis
                        return False, f"Missing opening parenthesis.", None
            else:
                # if there is no character after the matched number the analysis is done
                string_analysed = True
        else:
            # If no number can be found, there has to be an opening or closing parenthesis
            if string[0] == "(":
                # In case of an opening parenthesis the string after the parenthesis is given to this function
                # for the analysis through the corresponding closing parenthesis.
                sequence_string, sequence_numbers, sequence_operators = _analyse_string(string[1:], level + 1)

                # In case of an error the sequence_string is the type boolean with the value False
                if type(sequence_string) == bool and sequence_string == False:
                    return sequence_string, sequence_numbers, sequence_operators

                # The returned numbers and operators are added to the corresponding lists
                numbers.append(sequence_numbers)
                operators.append(sequence_operators)

                # and the rest of the string to analyze too
                string = sequence_string

                if len(string) > 0:
                    # If there are still characters, it is possible that there is an operator after the closing parenthesis
                    if string[0] in ["+", "-", "*", "/"]:
                        operators.append(string[0])
                        string = string[1:]
                else:
                    # if there is no character after the closing parenthesis the analysis is done
                    string_analysed = True
            elif string[0] == ")":
                # In case of a closing parenthesis it is checked if we are in a greater level than 0
                if level > 0:
                    # In this case we can return the string without the closing parenthesis and the collected numbers and operators
                    return string[1:], numbers, operators
                else:
                    # If we are in level 0 there has to be a missing opening parenthesis
                    return False, f"Missing opening parenthesis.", None
            else:
                # If there is no opening or closing parenthesis an error would be returned
                return False, f"The character \"{string[0]}\" in the substring \"{string}\" is not expected.", None

    # If the analysis is done because the end of the string,
    # a check is required if we are in level 0.
    if level != 0:
        return False, "Missing closing parenthesis.", None
    else:
        return True, numbers, operators


def _solve_equation(numbers, operators):
    if any(isinstance(item, list) for item in numbers):
        numbers_list_indices = [i for i, x in enumerate(numbers) if isinstance(x, list)]
        operators_list_indices = [i for i, x in enumerate(operators) if isinstance(x, list)]

        for i, index in reversed(list(enumerate(numbers_list_indices))):
            result, numbers[numbers_list_indices[i]] = _solve_equation(numbers[numbers_list_indices[i]], operators[operators_list_indices[i]])

            if not result:
                return False, numbers
            operators.pop(operators_list_indices[i])

    while "*" in operators or "/" in operators:
        try:
            operator_index_multi = operators.index("*")
        except ValueError:
            operator_index_multi = len(operators)+1

        try:
            operator_index_div = operators.index("/")
        except ValueError:
            operator_index_div = len(operators)+1

        if operator_index_multi > operator_index_div:
            try:
                if numbers[operator_index_div + 1] == 0:
                    raise ZeroDivisionError
                numbers[operator_index_div] = numbers[operator_index_div] / numbers[operator_index_div + 1]
                operators.pop(operator_index_div)
                numbers.pop(operator_index_div + 1)
            except ZeroDivisionError:
                return False, "Division by zero error."
        else:
            numbers[operator_index_multi] = numbers[operator_index_multi] * numbers[operator_index_multi+1]
            operators.pop(operator_index_multi)
            numbers.pop(operator_index_multi+1)

    while "+" in operators or "-" in operators:
        try:
            operator_index_add = operators.index("+")
        except ValueError:
            operator_index_add = len(operators) + 1

        try:
            operator_index_sub = operators.index("-")
        except ValueError:
            operator_index_sub = len(operators) + 1

        if operator_index_add > operator_index_sub:
            numbers[operator_index_sub] = numbers[operator_index_sub] - numbers[operator_index_sub + 1]
            operators.pop(operator_index_sub)
            numbers.pop(operator_index_sub + 1)
        else:
            numbers[operator_index_add] = numbers[operator_index_add] + numbers[operator_index_add + 1]
            operators.pop(operator_index_add)
            numbers.pop(operator_index_add + 1)

    if len(numbers) == 1:
        return True, numbers[0]
    else:
        return False, "Something went wrong."


def _check_numbers_operators_count(numbers, operators):
    if any(isinstance(item, list) for item in numbers):
        numbers_list_indices = [i for i, x in enumerate(numbers) if isinstance(x, list)]
        operators_list_indices = [i for i, x in enumerate(operators) if isinstance(x, list)]

        for i, index in reversed(list(enumerate(numbers_list_indices))):
            result = _check_numbers_operators_count(numbers[numbers_list_indices[i]], operators[operators_list_indices[i]])

            if not result:
                return False
            operators.pop(operators_list_indices[i])

    if len(operators) == len(numbers) - 1:
        return True
    else:
        return False


@click.group()
def cli():
    pass

@click.command()
@click.argument("operation")
def calculate(operation: str):

    # Prepare the given String
    result, string = _prepare_string(operation)

    if not result:
        click.echo(string, err=True)
        return

    result, numbers, operators = _analyse_string(string, 0)
    if not result:
        click.echo(numbers, err=True)
        return

    # Change type of the numbers from string to Int or Float
    result, numbers = _change_type_to_numeric(numbers)
    if not result:
        click.echo(numbers, err=True)
        return

    result = _check_numbers_operators_count(copy.deepcopy(numbers), copy.deepcopy(operators))
    if not result:
        click.echo(f"An operator is missing in the expression \"{operation}\".", err=True)
        return

    result, numbers = _solve_equation(numbers, operators)
    if not result:
        click.echo(numbers, err=True)
        return

    result, message = _result_output_handler(operation, numbers)
    if not result:
        click.echo(message, err=True)



@click.command()
@click.option("--get-history", "flag", flag_value="get_history")
@click.option("--clean-history", "flag", flag_value="clean_history")
@click.option("--get-variables", "flag", flag_value="get_variables")
@click.option("--set-variable", type=(str, str))
@click.option("--delete-variable", type=str, multiple=True)
@click.option("--clean-variables", "flag", flag_value="clean_variables")
@click.option("--get-constants", "flag", flag_value="get_constants")
def menu(flag, set_variable, delete_variable):
    message = ""
    if flag == "get_history":
        result, history = _get_history()
        if history:
            for element in history:
                message += f"{element.split("\t")[0]}\t{element.split("\t")[1].strip("\n")}\n"
        else:
            message = "No history created."
    elif flag == "clean_history":
        result, message = _clear_history()
    elif set_variable:
        name, value = set_variable
        result, message = _set_variables(name, value)
    elif flag == "get_variables":
        result, variables = _get_variables()
        if result:
            for key, value in variables.items():
                message += f"{key} = {value}\n"
        else:
            message = variables
    elif flag == "get_constants":
        result, variables = _get_constants()
        if result:
            for key, value in variables.items():
                message += f"{key} = {value}\n"
        else:
            message = variables
    elif delete_variable:
        names = delete_variable
        result, message = _delete_variable(names)
    elif flag == "clean_variables":
        result, message = _clean_variables()
    else:
        result = False
        message = "Unknown flag \"{flag}\""

    click.echo(message, err=not result)


cli.add_command(calculate)
cli.add_command(menu)

if __name__ == '__main__':
    cli()