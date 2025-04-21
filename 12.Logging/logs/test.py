from logger import logging

def add(a,b):
    logging.debug("Addition is taking place")
    return a + b

logging.debug("Addition function has been called")
add(2,5)