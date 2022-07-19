import logging
from functools import wraps


# Декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

def decor_logger(foo):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('logs/logfile.log')
    format_logger = logging.Formatter('%(asctime)s - [%(levelname)s] - [%(name)s] %(message)s')
    handler.setFormatter(format_logger)
    logger.addHandler(handler)

    @wraps(foo)
    def new_foo(*args, **kwars):
        logger.warning(f'Starting function {foo.__name__}')
        result = foo(*args, **kwars)
        logger.info(f'Значение {result}')
        logger.warning('Ending!')
        return result

    return new_foo
