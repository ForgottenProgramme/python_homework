def simple_decorator(func_to_decorate):
    def wrapper_func(*args, **kwargs):
        print("<3")
        func_to_decorate(*args, **kwargs)
        print("<3")

    return wrapper_func

@simple_decorator
def greetings(name: str):
    print(f"Hello, {name}!\n")
    return name.upper()

# greetings("mahe")

def math(num1: int, num2: int):
    print(num1)
    return num1+num2

math=simple_decorator(math)
# math(3,4)


def complex_decorator_outer_func(pre: str, post: str):
    def complex_decorator(func_to_decorate):
        def wrapper_func(*args, **kwargs):
            print(pre)
            func_to_decorate(*args, **kwargs)
            print(post)       
        return wrapper_func
    return complex_decorator



@complex_decorator_outer_func("starting", "ending")
def goodbye(name: str):
    print(f"Bye, {name}!\n")
    return name.upper()

goodbye("Mahe")