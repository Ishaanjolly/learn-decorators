
def decorator_name(func):
    """
    Basic decorator structure thanks to Chat GPT
    
    """
    def wrapper(*args, **kwargs):
        # Code to execute before the function call
        print("Before function call")
        
        result = func(*args, **kwargs)  # Call the original function
        
        # Code to execute after the function call
        print("After function call")
        
        return result  # Return the result of the function
    return wrapper


def error_catcher(func): 
    """
    try and except block for error catching 
    """
    def wrapper(*args, **kwargs):
        # Code to execute before the function call
        print("Before function call")
        
        try: 
        
            result = func(*args, **kwargs)  # Call the original function
            
            return result
            
        except Exception as e: 
            print("An error occured")
    
    return wrapper


def repeat(num_times): 
    def decorator(func): 
        def wrapper(): 
            for _ in range(num_times): 
                result = func(*args, **kwargs)
            return result 
        return wrapper 
    return decorator


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

  

# @decorator_function
# def say_hello():
#     print("Hello!")

# say_hello()
