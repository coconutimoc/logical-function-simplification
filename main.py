import logical_function as lf
import re


if __name__ == "__main__":

    print("Enter a logicial expression:\neg: a*b*not(c)+a*not(b)*c+not(a)*b*c+a*b*c")

    try:

        e = input(">>> ")

        function = lf.logical_function(e)

        print("Simplest expression:",function.simplify())
        print(function.variables)

    except KeyboardInterrupt:

        pass