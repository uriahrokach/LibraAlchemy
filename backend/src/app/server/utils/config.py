from types import SimpleNamespace
from functools import lru_cache
import json
import os


@lru_cache(maxsize=1)
def get_config():
    """
    Configs the alchemy system configurations.

    :return: The config dictionary.
    """
    try:
        env = os.environ['CONF']
    except KeyError:
        env = 'server/config/develop.json'

    with open(env, 'r', encoding='utf8') as conf_file:
        config = conf_file.read()
    config = json.loads(config, object_hook=lambda d: SimpleNamespace(**d))

    return config
