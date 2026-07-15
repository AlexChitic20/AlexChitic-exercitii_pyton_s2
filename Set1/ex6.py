def camel_to_snake(text):
    
    result = ""
    for index, char in enumerate(text):
        if char.isupper():
            if index > 0:
                result += "_"
            result += char.lower()
        else:
            result += char
    return result


if __name__ == "__main__":
    print(camel_to_snake("HelloWorld"))      # hello_world
    print(camel_to_snake("ThisIsATest"))     # this_is_a_test
