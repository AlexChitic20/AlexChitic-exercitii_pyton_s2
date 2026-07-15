def has_special_characters(text):
    
    special_chars = "\r\t\n\a\b\f\v"
    for char in text:
        if char in special_chars:
            return True
    return False


if __name__ == "__main__":
    print(has_special_characters("hello\tworld"))  # True
    print(has_special_characters("hello world"))   # False
