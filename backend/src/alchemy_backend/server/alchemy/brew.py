from typing import List
from itertools import combinations

from database.models import Potion, Effect
from .effects import get_effects_by_ingredients


def get_potions_by_effects(reactions: List[Effect]) -> List[Potion]:
    """
    Calculates every combination of effects given, and produces a potion if exists.

    :param reactions: The list of effects to check on.
    :return: A list of all potions produced.
    """
    effect_combs = []
    for i in range(2, len(reactions) + 1):
        effect_combs += list(combinations(reactions, i))

    potions = []
    for effects in effect_combs:
        effects = sorted(effects, key=lambda effect: effect.id)
        potion = Potion.objects(effects=effects)
        if len(potion) != 0:
            potions.append(potion[0])

    return potions


def brew_potion(materials: List[str], technic: str) -> List[dict]:
    """
    Receives a list of materials and technics, and brews every potion that can be made of them.

    :param materials: The materials of the potion.
    :param technic: The technic of the potion.

    :return: A list of possible potions that can be brewed with these ingredients.
    """
    reactions = get_effects_by_ingredients(materials, technic)
    potions = Potion.objects(
        __raw__={
            "effects": {
                "$not": {"$elemMatch": {"$nin": [effect.id for effect in reactions]}}
            }
        }
    )
    return [potion.json() for potion in potions]
