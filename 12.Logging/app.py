import logging

logging.basicConfig(
    level=logging.DEBUG,
    format= '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithematicApp')

def add(a,b):
    result = a+b
    logger.debug(f"Addition of {a} and {b} = {result}")
    return result
  

def subtr(a,b):
    result = a-b
    logger.debug(f"Subtraction of {a} and {b} = {result}")
    return result


def mult(a,b):
    result = a*b
    logger.debug(f"Multiplication of {a} and {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Division of {a} and {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Error: Division by zero is not allowed")
        return None
    


add(2,3)
subtr(5,2)
mult(4,5)
divide(10,2)
divide(10/0)