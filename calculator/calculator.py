import click
import re
import os
import json

# https://de.wikipedia.org/wiki/Mathematische_Konstante
constants = {
    "pi": "3.14159265358979323846",
    "squareroot_2": "1.41421356237309504880",
    "squareroot_3": "1.73205080756887729352",
    "golden_ratio": "1.61803398874989484820",
    "euler": "2.71828182845904523536",
    "euler_mascheroni": "0.57721566490153286060",
    "apery": "1.20205690315959428539",
    "erdos_borwein": "1.60669515241529176378",
    "ramanujan_soldner": "1.45136923488338105028",
    "lemniskat": "2.62205755429211981046",
    "legendre": "1.08366",
    "laplace_limit": "0.66274341934918158097",
    "catalan": "0.91596559417721901505",
    "meissel_mertens": "0.26149721284764278375",
    "glaisher_kinkelin": "1.28242712910062263687",
    "cahen": "1.73205080756887729352",
    "sierpinski": "2.58498175957925321706",
    "landau_ramanujan": "0.76422365358922066299",
    "gieseking": "1.01494160640965362502",
    "bernstein": "0.28016949902386913303",
    "brun": "1.90216058",
    "twin_prime": "0.66016181584686957392",
    "golomb_dickman": "0.62432998854355087099",
    "chintschin": "2.68545200106530644530",
    "chintschin_levy": "1.18656911041562545282",
    "mills": "1.30637788386308069046",
    "liebs": "1.53960071783900203869",
    "niven": "1.70521114010536776428",
    "gaus_kusmin_wirsing": "0.30366300289873265859",
    "porter": "1.46707807943397547289",
    "chaitin": "0.0078749969978123844",
    "alladi_grinstead": "0.80939402054063913071",
    "feigenbaum_1": "4.66920160910299067185",
    "feigenbaum_2": "2.50290787509589282228",
    "fransen_robinson": "2.80777024202851936522",
    "lengyel": "1.09868580552518701",
    "hafner_sarnak_mccurley": "0.35323637185499598454",
    "backhouse": "1.45607494858268967139",
    "viswanath": "1.1319882487943",
    "embree_trefethen": "0.70258"
}

def __prepare_string(input_string):
    result_last_result, value_last_result = _get_last_result()
    result_variables, value_variables = _get_variables()
    result_constants, value_constants = _get_constants()

    if not result_last_result:
        return False, value_last_result
    if not result_variables:
        return False, value_variables
    if not result_constants:
        return False, value_constants

    # Sort variables by length of the variable name
    variable_list = list(value_variables.items())
    constant_list = list(value_constants.items())
    blocked_variable_names = variable_list + constant_list + [("res", value_last_result)]
    blocked_variable_names.sort(key=lambda x: len(x[0]), reverse=True)

    # Remove all whitespaces
    input_string = "".join(input_string.split())

    # Replace Result-Variable and all Variables of the Memory with actual value
    if "res" in input_string:
        input_string = input_string.replace("res", value_last_result)
    for name, value in blocked_variable_names:
        if name in input_string:
            input_string = input_string.replace(name, value)

    return True, input_string

def __write_history(operation, result):
    try:
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_history')):
            with open(os.path.join(os.path.dirname(__file__), 'calculator_history'), "a") as f:
                f.write(f"{operation}\t{result}\n")
        else:
            with open(os.path.join(os.path.dirname(__file__), 'calculator_history'), "w") as f:
                f.write(f"{operation}\t{result}\n")
        return True, f"History written successfully."

    except BaseException as e:
        return False, f"Something went wrong while writing history:\n{e}"

def _get_constants():
    return True, constants

def _get_history():
    try:
        history = []
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_history')):
            with open(os.path.join(os.path.dirname(__file__), 'calculator_history'), "r") as f:
                for line in f.readlines():
                    history.append(line)
        return True, history
    except BaseException as e:
        return False, f"Something went wrong while retrieving the history:\n{e}"

def _get_variables():
    try:
        variables = {}
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_variables')):
            with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "r") as f:
                variables = json.load(f)
        return True, variables
    except BaseException as e:
        return False, f"Something went wrong while retrieving the variables:\n{e}"

def _set_variables(name, value):
    if value == "res":
        result, value = _get_last_result()
        if not result:
            return False, value

    result, variables = _get_variables()
    if result:
        if name in variables.keys():
            return False, f"Variable-Name \"{name}\" already exists."
        elif name in constants.keys():
            return False, f"Variable-Name \"{name}\" must not be a constant."
        elif re.search(r'^[+\-]?[0-9]+\.?[0-9]*', name):
            return False, f"Variable-Name \"{name}\" must not be numeric."
        elif not re.search(r'^[+\-]?[0-9]+\.?[0-9]*$', value):
            return False, f"Variable-Value \"{value}\" has to be numeric."
        elif name == "res":
            return False, f"Variable-Name \"res\" is reserved."
        elif len(name.split()) != 1:
            return False, f"Whitespace are not allowed in the Variable-Name \"{name}\"."
        else:
            try:
                variables[name] = value
                with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "w") as f:
                    json.dump(variables, f)
                return True, f"Variable \"{name}\" has been set with value \"{value}\"."
            except BaseException as e:
                return False, f"Something went wrong while setting the variable:\n{e}"
    else:
        return False, variables

def _delete_variable(names):
    result, variables = _get_variables()

    message = ""
    for name in names:
        if result:
            if not name in variables.keys():
                message += f"Variable \"{name}\" does not exist.\n"
            else:
                try:
                    value = variables[name]
                    variables.pop(name)
                    if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_variables')):
                        with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "w") as f:
                            json.dump(variables, f)
                    message += f"Variable \"{name}\" with value \"{value}\" has been deleted.\n"
                except BaseException as e:
                    return False, f"Something went wrong during the deletion:\n{e}"
        else:
            return False, variables

    return True, message

def _clean_variables():
    variables = {}
    try:
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_variables')):
            with open(os.path.join(os.path.dirname(__file__), 'calculator_variables'), "w") as f:
                json.dump(variables, f)
        return True, f"Variables cleared successfully."
    except BaseException as e:
        return False, f"Something went wrong while cleaning the variables:\n{e}"

def _clear_history():
    try:
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'calculator_history')):
            with open(os.path.join(os.path.dirname(__file__), 'calculator_history'), "w") as f:
                f.write("")
        return True, f"History cleared successfully."
    except BaseException as e:
        return False, f"Something went wrong while clearing the history:\n{e}"

def _get_last_result():
    last_result = "0"
    result, history = _get_history()

    if result:
        if history:
            last_result = history[-1].split("\t")[-1].strip("\n")

        return True, last_result
    else:
        return False, history

def _change_type_to_numeric(string):
    # Change type of the Number from string to Int or Float
    try:
        if "." in string:
            return True, float(string)
        else:
            return True, int(string)
    except BaseException as e:
        return False, f"Something went wrong while changing the type to numeric:\n{e}"

def _result_output_handler(operation, value):
    if type(value) == float:
        value = round(value, 10)
        click.echo(value, err=False)
        result, message = __write_history(operation, value)
    elif type(value) == int:
        click.echo(value, err=False)
        result, message = __write_history(operation, value)
    else:
        result = False
        message = f"Unknown Type of the result {type(value)}"

    return result, message


@click.group()
def cli():
    pass

@click.command()
@click.argument("operation")
def calculate(operation: str):

    numbers = []
    operators = []
    string_analysed = False

    # Prepare the given String
    result, substring = __prepare_string(operation)

    if not result:
        click.echo({substring}, err=True)
        return

    # Start analysis
    while not string_analysed:

        # Search for the given pattern from the beginning of the String
        match = re.search(r'^[+\-]?[0-9]+\.?[0-9]*', substring)
        if match:

            # when there is a match, the number is added to the numbers-List
            numbers.append(substring[:match.regs[0][1]])
            if match.regs[0][1] + 1 <= len(substring):
                # as long there characters after the matched number,
                # the next character after the number is handled as an operator and added to the operators-List
                operators.append(substring[match.regs[0][1]:match.regs[0][1] + 1])

                substring = substring[match.regs[0][1] + 1:]
            else:

                # if there is no character after the matched number the analysis is done
                string_analysed = True
        else:
            # if there is no match, there should be a syntax-error in the given string
            click.echo(f"Substring \"{substring}\" contains an error.", err=True)
            return

    # Change type of the numbers from string to Int or Float
    for i, number in enumerate(numbers):
        result, numbers[i] = _change_type_to_numeric(number)

        if not result:
            click.echo(numbers[i], err=True)
            return

    # check the operators-List for unknown operators
    for operator in operators:
        if operator not in ["+", "-", "*", "/"]:
            click.echo(f"Unknown Operator \"{operator}\".", err=True)
            return

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
                click.echo(f"Division by zero error.", err=True)
                return
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
        result, message = _result_output_handler(operation, numbers[0])
        if not result:
            click.echo(message, err=True)
    else:
        click.echo(f"\"{operation}\" contains an error.", err=True)


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