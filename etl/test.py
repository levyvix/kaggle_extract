from decorators.utils import log_function, time_function


@time_function
@log_function
def test():
    print("test")


test()
