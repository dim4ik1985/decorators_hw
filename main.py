from decor_logger import decor_logger
from param_decor_logger import parametrized_decor_logger
import logging
import requests

if __name__ == '__main__':
    @decor_logger
    def sum(a, b):
        logger = logging.getLogger('decor_logger')
        logger.info("Аргументы %s и %s" % (a, b))
        return a + b


    sum(50, 15)

    HOST = 'https://swapi.dev/api/'


    @parametrized_decor_logger('log_func_swapi.log')
    def get_planet(planet_id):
        logger = logging.getLogger('param_decor_logger')
        logger.info(f'Аргумент {planet_id}')
        return requests.get(f'{HOST}planets/{planet_id}').json()["name"]


    get_planet(15)
