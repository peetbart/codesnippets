def extra(func):
    print '-extra-'

    def caller():
        func()

    return caller


def base_func():
    """original func you don't / can't modify """
    print '-base func running-'



base_func = extra(base_func)


# Original func call you can't / dont't want to modufy:
base_func()
