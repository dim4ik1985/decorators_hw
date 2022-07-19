import logging


# Декоратор-логгер, с параметром – путь к логам

def parametrized_decor_logger(parameter):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(f'logs/{parameter}')
    format_logger = logging.Formatter('%(asctime)s - [%(levelname)s] - [%(name)s] %(message)s')
    handler.setFormatter(format_logger)
    logger.addHandler(handler)

    def decor(foo):
        def new_foo(*args, **kwars):
            logger.warning(f'Starting function {foo.__name__}')
            result = foo(*args, **kwars)
            logger.info(f'Значение {result}')
            logger.warning('Ending!')
            return result

        return new_foo

    return decor
