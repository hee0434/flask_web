from functools import wraps

def without_wraps(func):
    def __wraper(*args, **kwargs):
        ''' This is test!! '''
        return func(*args, **kwargs)
    return __wraper

@without_wraps
def func_1():
    ''' This is test!! '''
    return "Hello"
    
# words = without_wraps(func_1).__name__
# print(words)

def with_wraps(func):
    @wraps(func)
    def __wraper(*args, **kwargs):
        ''' This is test!! '''
        return func(*args, **kwargs)
    return __wraper

@with_wraps
def func_1():
    ''' This is test!! '''
    return "Hello"

print(func_1.__doc__)
print(func_1.__name__)