def binary(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@binary
def convert_to_bin(number):
    divisior = 2
    result = 0
    category = 1
    while number > 0:
        cur_number = number % divisior
        result += cur_number*category
        number = number // divisior
        category *= 10
    print(result)