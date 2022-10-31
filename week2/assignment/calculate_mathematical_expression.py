def calculate_mathematical_expression(num1, num2, oper):
    opers = {"+": lambda x,y: x+y, "-": lambda x,y: x-y, ":": lambda x,y: x/y, "*": lambda x,y: x*y}
    if (oper not in opers.keys()) or (oper == ":" and num2 == 0):
        return None
    return opers[oper](num1, num2)

def calculate_from_string(oper_str):
    math_oper = oper_str.split(" ")
    return calculate_mathematical_expression(float(math_oper[0]), float(math_oper[2]), math_oper[1])