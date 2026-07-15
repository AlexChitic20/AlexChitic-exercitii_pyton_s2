def calculate(x, y, op):
    """Applies the operation `op` ("+", "-", "*", "/") on x and y."""
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        raise ValueError(f"Unknown operation: {op}")


if __name__ == "__main__":
    print(calculate(4, 2, "+"))  # 6
    print(calculate(4, 2, "/"))  # 2.0
