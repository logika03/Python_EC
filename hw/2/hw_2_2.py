def poman(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


@poman
def convert_arab_in_rim(number):
    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rim = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    result = ""
    while number > 0:
        while arab[i] <= number:
            result += rim[i]
            number -= arab[i]
        i += 1
    print(result)
