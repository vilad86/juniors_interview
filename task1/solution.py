from typing import Callable


def strict(func: Callable):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        #: Check positional arguments.
        for arg, (key, value) in zip(args, annotations.items()):
            if not isinstance(arg, value):
                raise TypeError(f"Argument '{key}' must be of type  {value}, got {type(arg)} instead.")

        #: Check named arguments.
        for key, value in kwargs.items():
            if (key not in annotations): continue

            expected_type = annotations[key]
            if not isinstance(value, expected_type):
                raise TypeError(f"Argument '{key}' must be of type  {value}, got {type(value)} instead.")
        
        return func(*args, **kwargs)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

#: Custom function.
@strict
def join_str(a: str, b: str) -> str:
    return a + b

@strict
def sum_float(a: float, b: float) -> float:
    return a + b

@strict
def invert_bool(a: bool) -> bool:
    return not a


if (__name__ == '__main__'):
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
