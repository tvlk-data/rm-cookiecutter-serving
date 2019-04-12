import logging
from functools import wraps

def monitor(func_name):
    def decorator(func):
        @wraps(func)
        def wrapper():
            logging.info(func_name)
            return func()
        return wrapper
    return decorator
