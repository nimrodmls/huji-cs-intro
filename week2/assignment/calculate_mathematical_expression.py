#################################################################
# FILE : additional_file.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex1 2023
# DESCRIPTION: Exporting maths utility functions
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

def calculate_mathematical_expression(num1, num2, oper):
    """
    Calculates basic math operations.
    Supporting the + (increment), - (decrement), : (division), * (multiplication) operators.
    num1 & num2 can either be integers or floating point numbers.
    """
    opers = {"+": lambda x,y: x+y, "-": lambda x,y: x-y, ":": lambda x,y: x/y, "*": lambda x,y: x*y}
    if (oper not in opers.keys()) or (oper == ":" and num2 == 0):
        return None
    return opers[oper](num1, num2)

def calculate_from_string(oper_str):
    """
    Calculates basic math operations from a given string.
    The string format should be {num1} {oper} {num2}.
    {oper} supports the + (increment), - (decrement), : (division), * (multiplication) operators
    num1 & num2 can either be integers or floating point numbers.
    """
    math_oper = oper_str.split(" ")
    return calculate_mathematical_expression(float(math_oper[0]), float(math_oper[2]), math_oper[1])
