from itertools import combinations
from typing import List, Dict
from mongoengine import DoesNotExist

from database.models import PotionType, Effect, Potion


def get_types_names() -> List[str]:
    """
    Fetches a list of all exiting potion types names.

    :return: The names of all potion types.
    """
    return [p_type.name for p_type in PotionType.objects]


def get_type_by_name(name: str) -> dict:
    """
    Returns a potion type by it's given name.

    :param name: The name of the potion type.
    :return: The whole potion type as a JSON object.
    """
    try:
        potion_type = PotionType.objects.get(name=name)
    except DoesNotExist:
        raise KeyError(f"PotionType {name} does not exist.")

    return potion_type.json()


def get_types_by_effects(effects: List[str]) -> List[Dict[str, str]]:
    """
    Returns all potion types created by correlating effects.

    :param effects: The effects to check the potion types of.
    :return: ALl potion types that correlate to the given effects.
    """
    try:
        effects = [Effect.objects.get(name=effect) for effect in effects]
    except DoesNotExist:
        raise KeyError(f'One or more of effects {",".join(effects)} does not exist.')

    potion_types = []
    for effect_a, effect_b in combinations(effects, 2):
        new_potion_type = PotionType.objects(effects__all=[effect_a, effect_b])
        potion_types += new_potion_type

    return [p_type.json() for p_type in potion_types]


def get_types_by_potion(potion: str) -> List[Dict[str, str]]:
    """
    Returns the potion types of a potion.

    :param potion: The name of the potion.
    :return:  ALl potion types that correlate to the given potion.
    """
    try:
        potion = Potion.objects.get(name=potion)
    except DoesNotExist:
        raise KeyError(f"Potion {potion} does not exist.")
    return get_types_by_effects([effect.name for effect in potion.effects])
