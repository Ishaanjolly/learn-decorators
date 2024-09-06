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
6. Logging track 
7. 

Other coding practices that I should look at:
1. Async - writing code that allows me to run other code whilst wokring on something else 


Stuff to look at: 
1. https://github.com/micheles/decorator & https://pypi.org/project/decorators/ for more examples
2. https://github.com/Jaymon/decorators
3. https://medium.com/python-in-plain-english/python-decorators-junior-vs-intermediate-vs-senior-vs-expert-7a23049082e0
4. https://medium.com/@mysteryweevil/mastering-class-decorators-in-python-a-practical-guide-eb3fb7554113
5  https://medium.com/python-in-plain-english/i-doubled-my-flask-apps-efficiency-with-these-10-python-decorators-591207e1b136
6. https://medium.com/gitconnected/python-decorators-distinguishing-junior-intermediate-senior-and-expert-levels-a12a70ddd919 
7. https://medium.com/gitconnected/decorators-vs-inheritance-when-to-use-each-in-python-815713ca2c26
8  https://medium.com/gitconnected/most-used-python-decorators-when-to-use-and-when-not-to-32b8f883ee43



