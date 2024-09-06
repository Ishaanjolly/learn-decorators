def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
