"""
example for decorators.
"""


def decor(func):
    def wrapper():
        print '::before'
        result = func()
        print '::after'
        return result

    return wrapper


@decor
def base_func():
    print '-base func running-'





if __name__ == '__main__':
    base_func()
