from functools import wraps

def value(lmbd):
    @wraps(lmbd)
    def checkup(func):
        def wrapper(num):
            if lmbd(num):
                result = func(num)
                return result
            else:
                raise ValueError
        return wrapper
    return checkup

@value(lambda num: num > 0)
def calc_cube(num):
    return int(num)**3


try:
    print(calc_cube(-5))
except ValueError:
    print('Wrong val')