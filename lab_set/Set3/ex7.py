FUNCTIONS = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k),
}


def apply_function(name, *args, **kwargs):
    """Applies the function named `name` (looked up in the global
    FUNCTIONS dictionary) over the received arguments. Adding a new
    function to FUNCTIONS doesn't require any change to this function,
    since any combination of *args / **kwargs is passed through."""
    return FUNCTIONS[name](*args, **kwargs)


if __name__ == "__main__":
    apply_function("print_only_args", 1, 2, 3)
    apply_function("print_only_kwargs", x=1, y=2)
    apply_function("print_all", 1, 2, x=3)
