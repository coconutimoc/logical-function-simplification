import _init_class
import numpy as np
import re


class logical_function:
    
    def __init__(self,expression:str=None,truth_table:list=[]):

        #raise error if input is legal
        assert expression != None or truth_table != [], "Error: initialize a logical function with no attributes."

        assert expression == None  or truth_table == [], "Error: should initialize with only one attribute."

        check = len(truth_table)

        while check > 1:

            assert check % 2 == 0, "Error: table length should be exponential of two."

            check = check // 2

        #initialize the object when expression is given
        if expression != None:

            expression = re.sub("\s","",expression)

            self.expression = expression

            self.truth_table = _init_class.expression_to_table(expression)

            self.variables = _init_class.variables(expression)

        #initialize the object when truth table is given
        elif expression == None:

            self.truth_table = truth_table
           
            self.variables = _init_class.variables(truth_table=truth_table)

            self.expression = self.simplify()


    def _minterms_of_implicant_(self, implicant:int) -> list:

        """return a list that includes all the minterms in an implication"""

        minterms = []

        for minterm in range(0,int(np.power(2,len(self.variables)))):

            check = 1

            for pos in range(1,len(self.variables)+1):

                if (implicant // np.power(3,len(self.variables)-pos)) % 3!=2:

                    if (minterm >> (len(self.variables) - pos))%2 != (implicant // np.power(3,len(self.variables)-pos)) % 3:
                        
                        check *= 0 

            if check == 1:
                
                minterms.append(minterm)

        return minterms
    

    def simplify(self):
        """simplify the expression of logical function. \n
        the result will bind to the simplest_functon attribute
        """

        ##return the simplest function attribute if the function has been called once

        if hasattr(self,"simplest_expression") == 1:

            return self.simplest_expression
        
        ##if it's the first time simplify being called, then calculate the simplest function

        #initialize a list that record how many times a minterm(complination of variables) has been circled
        circled = [0 for x in self.truth_table]

        #initilize a list that receive prime implicants
        implicant_receive = []

        #initilize a list that include all possible implicants
        #the less variable an implicant includes,the earlier an implicant is poped
        implicant_pop = np.load(f"implicant/m_is_{len(self.variables)}.npy")

        #check whether the implicant poped is prime implicant
        #squeeze all the prime implicant into simplest_expression
        for implicant in implicant_pop:

            minterms = self._minterms_of_implicant_(implicant)

            check_true = 1

            check_circled = 1

            for minterm in minterms:

                if self.truth_table[minterm] == 0:
                    
                    check_true *= 0

                if circled[minterm] == 0:

                    check_circled *= 0

            if check_true == 1 and check_circled == 0:

                implicant_receive.append(implicant)

                for minterm in minterms:

                    circled[minterm] += 1

        implicant_receive = list(implicant_receive)

        implicant_biggest = []
        
        #delete the prime implicants that are not biggest
        for implicant in implicant_receive[::-1]:

            minterms = self._minterms_of_implicant_(implicant)

            check_circled = 1

            for minterm in minterms:

                if circled[minterm] == 1:

                    check_circled *= 0

            if check_circled == 1:

                for minterm in minterms:
                    
                    circled[minterm] -= 1

            else:

                implicant_biggest.append(implicant)

        ##convert the result to string
        simplest_expression = ""
        
        for implicant in implicant_biggest:

            for pos in range(1,len(self.variables)+1):

                if (implicant // np.power(3,len(self.variables)-pos) )% 3 ==  0:

                    simplest_expression += f"not({self.variables[pos-1]})*"

                elif (implicant//np.power(3,len(self.variables)-pos))%3 == 1:

                    simplest_expression += f"{self.variables[pos-1]}*"

            simplest_expression = simplest_expression.rstrip("*") + "+"

        simplest_expression = simplest_expression.rstrip("+")

        self.simplest_expression = simplest_expression

        return simplest_expression
    

if __name__ == "__main__":

    #e = "a*b"
    #e = "a*b+c"
    #e = "not(a)+not(b)*(a*c+not(b))"
    e = "A*B*C+A*B*not(C)+not(A)*C+B*C"
    #e = "a*b*not(c)+a*not(b)*c+not(a)*b*c+a*b*c"

    print("Expression:",e)

    function = logical_function(e)

    print("Simplest expression:",function.simplify())