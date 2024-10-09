import re
import numpy as np


def expression_to_table(expression:str) -> list:
    """calculate the truth table of a logical expression"""

    _truth_table = []

    _variables = variables(expression)

    variable_amount = len(_variables)

    for minterm in range(0,np.power(2,variable_amount)):

        _expression = expression

        variable = 0

        while variable < variable_amount:

            #substitude variables with bools
            v = _variables[variable]
            _expression = _expression.replace(v,str((minterm // int(np.power(2,variable_amount - variable - 1))) % 2))
            variable += 1

        #substitude "+" with "or"
        _expression = re.sub("\+"," or ",_expression)

        #substitude "*" with "and"
        _expression = re.sub("\*"," and ",_expression)

        _truth_table.append(int(eval(_expression)))

        

    print("Truth table:",_truth_table)

    return _truth_table


def variables(expression:str=None,truth_table:list=[]) -> list:
    """identify all the variables used in an expression or truth table\n
    and return a list that contain them
    """

    _variables = []

    if expression != None:

        for _variable in re.finditer("[^(not)|\(|\)|\*|\+]",expression):

            if _variable.group() not in _variables:
            
                _variables.append(_variable.group())

    elif expression == None:

        _variable_amount = int(np.log(len(truth_table))/np.log(2))

        for _variable in range(1,_variable_amount + 1):

            _variables.append(f"A{_variable}")

    return _variables


if __name__ == '__main__':
    print(expression_to_table("a*b+c"))