Typical wrapper structure: 

```
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Code to execute before the function call
        print("Before function execution")
        
        result = func(*args, **kwargs)  # Call the original function
        
        # Code to execute after the function call
        print("After function execution")
        
        return result  # Return the result of the original function
    return wrapper

```

Kinds of wrappers:

1. Wait 
2. Retry 
3. Repeat 
4. Wait and retry 
5. Catch errors


Repositories to look at:
1. https://github.com/micheles/decorator & https://pypi.org/project/decorators/ for more examples


