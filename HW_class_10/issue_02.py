import sys
from datetime import datetime


def timed_output(function):
    original_write = sys.stdout.write

    def my_write(string_text):
        current_datetime = datetime.now()
        time_format = "%Y-%m-%d %H:%M:%S"
        if string_text != '\n':
            string_text = f'[{current_datetime:{time_format}}]: {string_text}'
        original_write(string_text)

    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write
        return result

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')
    print(f'Hello, {name}!')

print_greeting("Nikita")

