import logical_function as lf
import re
import numpy as np


if __name__ == "__main__":

    print("Logical Function Simplifier interactive mode")

    function = None

    while True:

        command = input(">>> ")

        if re.match(r"exit",command):

            exit()

        elif re.match(r"help",command):

            print("Commands:")
            print("expression [expression]: initialize a logical function with an expression")
            print("table [table]: initialize a logical function with a truth table")
            print("simplify: simplify the logical function")
            print("exit: exit the program")

        elif re.match(r"expression",command):

            function = lf.logical_function(command.split()[1])
            print(function.truth_table)
            print("Simplest expression:",function.simplify())
            print(function.variables)
        
        elif re.match(r"table",command):

            iterator = re.finditer("\d",command.split()[1])

            table = [int(i.group()) for i in iterator]

            function = lf.logical_function(truth_table=table)

            print(function.truth_table)
            print("Simplest expression:",function.simplify())
            print(function.variables)