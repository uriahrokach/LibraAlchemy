from mongoengine.errors import DoesNotExist
from itertools import combinations
from typing import List

from ...database.models import Effect
from ..utils.consts import TECHNIC_MATERIAL_LENGTH


def get_effects_by_name(name: str) -> List[dict]:
    """
    Receives a name of an effect, than gets the whole effect.

    :param name: The name of the effect.
    :return: The effect.
    """
    effects = Effect.objects(name=name)
    if len(effects) == 0:
        raise KeyError(f'Effect {name} does not exist')

    return [effect.json() for effect in effects]


def get_effects_by_ingredients(materials: List[str], technic: str) -> List[Effect]:
    """
    Gets the effect from a list of ingredients.

    :param materials: the materials of the effect.
    :param technic:  the technic of the effect.

    :return: a list of the created effects.
    """
    reactions = []
    for materials in combinations(set(materials), TECHNIC_MATERIAL_LENGTH):
        try:
            reactions.append(Effect.objects.get(technic=technic, materials=sorted(materials)))
        except DoesNotExist:
            raise KeyError(f'Effect with technic {technic} and materials {", ".join(materials)} does not exist.')

    return reactions
