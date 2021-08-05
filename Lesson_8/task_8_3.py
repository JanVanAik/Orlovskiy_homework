from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            markup = func(arg)
            res = f'{arg}: {type(arg)} \n{markup}'
            return res
    return wrapper


@type_logger
def calc_cube(num):
    return int(num)**3


print(calc_cube(5))
