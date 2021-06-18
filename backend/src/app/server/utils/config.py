import os

TEST_CONFIG = {
    'MATERIALS': ['לוטוס דם', 'דרדר דרקון', 'פטריות מעמקים', 'תפרחת השעווה', 'שורש אלף אצילי', 'לילית שחורה', 'קשקשי לטאת ענק'],
    'TECHNICS': ['בישול', 'ייבוש וכתישה', 'התססה', 'חליטה'],
    'DB_CONFIG': 'mongodb://localhost:27017/alchemy_test'
}

PROD_CONFIG = {
    'MATERIALS': [],
    'TECHNICS': [],
    'DB_CONFIG': 'mongodb://localhost:27017/alchemy_prod'
}


def get_config(env: str = None):
    """
    Configs the alchemy system configurations.

    :param env: the environment to run. Defaults to the environment variable ENV. or the test env.
    :return: The config dictionary.
    """
    if not env:
        try:
            env = os.environ['ENV']
        except KeyError:
            env = None
    if not env or env == 'test':
        return TEST_CONFIG
    return PROD_CONFIG
