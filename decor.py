"""
example for decorators.
"""


def decor_alksdfalskdjfhaljkhf(func):
    def wrapper_uyeryryryryryry():
        print '::before'
        result = func()
        print '::after'
        return result

    return wrapper_uyeryryryryryry


@decor_alksdfalskdjfhaljkhf
def base_func():
    print '-base func running-'





if __name__ == '__main__':
    base_func()
