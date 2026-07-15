import re


def evaluate_polynomial(polynomial, value):
  
    # Remove all spaces to make the pattern simpler to match.
    text = polynomial.replace(" ", "")

    # Each term looks like: sign(optional) coefficient(optional) x(optional) ^exponent(optional)
    term_pattern = re.compile(r"([+-]?)(\d*)(x)?(?:\^(\d+))?")

    total = 0
    for sign, coeff_text, has_x, exponent_text in term_pattern.findall(text):
        if sign == "" and coeff_text == "" and has_x == "":
            continue  # empty match from the regex engine, skip it

        sign_value = -1 if sign == "-" else 1
        coefficient = int(coeff_text) if coeff_text != "" else 1

        if has_x:
            exponent = int(exponent_text) if exponent_text else 1
        else:
            exponent = 0

        total += sign_value * coefficient * (value ** exponent)

    return total


if __name__ == "__main__":
    print(evaluate_polynomial("3x ^ 3 + 5x ^ 2 - 2x - 5", 2))
    # 3*8 + 5*4 - 2*2 - 5 = 24 + 20 - 4 - 5 = 35
