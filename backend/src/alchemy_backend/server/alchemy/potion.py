from mongoengine.errors import DoesNotExist, NotUniqueError
from typing import List
import re

from database.models import Potion, PotionType
from .effects import get_effects_by_ingredients


def set_potion(name: str, materials: List[str], technic: str, description: str) -> None:
    """
    Creates a new potion in the database.

    :param name: the name of the potion.
    :param materials: the materials of the potion.
    :param technic: the technic of the potion.
    :param description: the description of the potion.
    """
    effects = get_effects_by_ingredients(materials, technic)
    effects = sorted(effects, key=lambda effect: effect.id)
    potion = Potion(name=name, effects=effects, description=description)
    try:
        potion.save()
    except NotUniqueError:
        raise ValueError(f"Potion {name} already exists.")


def get_potions_by_name_regex(name: str = None) -> List[Potion]:
    """
    Gets the potions who's names contain the regex name given.

    :param name: the regex name of the potion.
    :return: The list of the potion.
    """
    pattern = re.compile(f".*{name}.*")
    return [potion for potion in Potion.objects(name=pattern)]


def get_potion_by_name(name: str) -> dict:
    """
    Returns a potion by it's given name.

    :param name: The name of the potion.
    :return: The whole potion.
    """
    try:
        potion = Potion.objects.get(name=name)
    except DoesNotExist:
        raise KeyError(f"Potion {name} does not exist.")

    return potion.json()


def delete_potion(name: str) -> None:
    """
    Deletes a potion from the DB.

    :param name: The name of the potion to delete.
    """
    try:
        potion = Potion.objects.get(name=name)
    except DoesNotExist:
        raise KeyError(f"Potion {name} does not exist")

    potion.delete()


def validate_str_field(value: str, field: str):
    if value == "":
        raise ValueError(f"{field} cannot be empty.")
    if value[0] == " " or value[-1] == " ":
        raise ValueError(f"{field} cannot start or end with a space.")


def get_potions_by_type(potion_type: str):
    try:
        p_type = PotionType.objects.get(name=potion_type)
    except DoesNotExist:
        raise KeyError(f"Potion type {potion_type} does not exist")

    potions = Potion.objects(effects__all=p_type.effects)
    return [potion.json() for potion in potions]


# def get_recipes(potion_name: str):
#     effects = Potion.objects.get(name=potion_name).effects
#     combinations = []
#     for effect in effects:
#         for effect.reactions
#         reactions.append(effect.reactions)
