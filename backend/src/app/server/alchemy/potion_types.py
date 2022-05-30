from itertools import combinations
from typing import List
from mongoengine import NotUniqueError, DoesNotExist

from ...database.models import PotionType, Effect


def create_type(name: str, effects: List[str], description: str) -> None:
    effects = [Effect.objects.get(name=effect) for effect in effects]
    effects = sorted(effects, key=lambda effect: effect.id)
    potion_type = PotionType(name=name, effects=effects, description=description)
    try:
        potion_type.save()
    except NotUniqueError:
        raise ValueError(f'PotionType {name} already exists.')


def delete_type(name: str) -> None:
    """
    Deletes a potion type from the DB.

    :param name: The name of the potion to delete.
    """
    try:
        potion_type = PotionType.objects.get(name=name)
    except DoesNotExist:
        raise KeyError(f"PotionType {name} does not exist")

    potion_type.delete()


def get_type_by_name(name: str) -> dict:
    """
    Returns a potion type by it's given name.

    :param name: The name of the potion type.
    :return: The whole potion type as a JSON object.
    """
    try:
        potion_type = PotionType.objects.get(name=name)
    except DoesNotExist:
        raise KeyError(f'PotionType {name} does not exist.')

    return potion_type.json()


def get_types_by_effects(effects: List[str]) -> List[PotionType]:
    effects = [Effect.objects.get(name=effect) for effect in effects]

    potion_types = []
    for effect_a, effect_b in combinations(effects, 2):
        new_potion_types = list(set(PotionType.objects(effects=effect_a)) & set(PotionType.objects(effects=effect_a)))
        potion_types += new_potion_types

    return potion_types

