# Here I want to write a decorator function that does function practical while accepting arguments

# Maybe I can write a decorator that calculates and prints the time a function takes to run. It accepts the desired unit of time 
# (ms or s) as two possible arguments


def time_calculator(unit: str = "s"):
    """A decorator that accepts 's' or 'ms' as arguement. 's' is default if not argument is passed."""
    import time
    def decorator_wrapper(func_to_decorate):
        def func_wrapper(*args, **kwargs):
            start_t = time.time()
            func_to_decorate(*args, *kwargs)
            end_t= time.time()
            if unit=="s":
                time_taken=end_t-start_t
            else:
                time_taken=end_t-start_t/1000
            
            print(f"{time_taken} {unit}")
        return func_wrapper
    return decorator_wrapper

@time_calculator("ms")
def a_complex_function(number: int):
    import math
    print(math.factorial(number))

a_complex_function(18)
    