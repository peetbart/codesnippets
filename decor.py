def extra(func):
    """
    This is the function that returns the new function
    that wraps your original function and calls it
    when you make a call with the original function's name
    your original function is an argument "func" & gets called
    when this function is called, which happend when the
    original name is called.
    """

    def caller():
        # Put extra code BEFORE you run you original func
        print '-extra before-'
        result = func()
        print '-extra after-'
        # Put extra code AFTER you run you original func

    return caller


# This syntax: "@"; the decorator is just a syntactic
# sugar to do the same as the variable assignment below
@extra
def base_func():
    """original func you don't / can't modify """
    print '-base func running-'



# # you put your original function call in another
# # function, so you can leave the original func
# # and calling it untouched.
# base_func = extra(base_func)


# Original func call you can't / dont't want to modufy:
base_func()
