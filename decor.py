def extra(func):
    print '-extra-'

    def caller():
        func()

    return caller


def base_func():
    print '-base func running-'

base_func = extra(base_func)


base_func()
