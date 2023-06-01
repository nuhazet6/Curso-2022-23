import re

exp = "3.2 + 4.3"
regex = r"^\s*(\d+(?:.\d+)?)\s*([+\-*/])\s*(\d+(?:.\d+)?)\s*$"

if m := re.search(regex, exp):
    left_oper, operator, right_oper = m.groups()
    left_oper = float(left_oper)
    right_oper = float(right_oper)
    match operator:
        case "+":
            result = left_oper + right_oper
        case "*":
            result = left_oper * right_oper
        case "/":
            result = left_oper / right_oper
        case "-":
            result = left_oper - right_oper
print(exp, result)
