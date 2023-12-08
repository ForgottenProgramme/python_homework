# I want to write a decorator that accepts arguement and does something meaningful with these arguments. 

# a decorator that takes arguements 
def singer_decorator(arg1):
    def decorator_wrapper(func):
        def func_wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(arg1)
        return func_wrapper
    
    return decorator_wrapper

@singer_decorator("A mug of hot chocolate.")
def say_something_about_the_singer(name: str):
    print(f"{name}'s voice is like:")

say_something_about_the_singer("Iffat")


