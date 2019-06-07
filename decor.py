def extra(func):
    print '-extra-'

    def caller():
        func()

    return caller


def base_func():
    """original func you don't / can't modify """
    print '-base func running-'



# you put your original function call in another
# function, so you can leave the original func
# and calling it untouched.
base_func = extra(base_func)


# Original func call you can't / dont't want to modufy:
base_func()
