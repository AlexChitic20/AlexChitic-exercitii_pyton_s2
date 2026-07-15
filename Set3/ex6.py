OPERATORS = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
}


def apply_operator(operator, a, b):
   
    return OPERATORS[operator](a, b)


if __name__ == "__main__":
    print(apply_operator("+", 3, 4))   # 7
    print(apply_operator("*", 3, 4))   # 12

    # Adding a new operator doesn't require touching apply_operator:
    OPERATORS["-"] = lambda a, b: a - b
    print(apply_operator("-", 10, 3))  # 7
