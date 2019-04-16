import logging
from functools import wraps
import google.cloud.logging

def initStackdriverLogging():
    client = google.cloud.logging.Client()
    client.setup_logging()

def monitor(func_name):
    def decorator(func):
        @wraps(func)
        def wrapper():
            handler = logging.StreamHandler()
            handler.terminator = ""
            logging.info("[RM-MONITORING] " + func_name)
            return func()
        return wrapper
    return decorator
