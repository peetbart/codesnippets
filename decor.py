def extra():
    print '-extra-'


def base_func():
    print '-base func running-'

base_func = extra


base_func()
