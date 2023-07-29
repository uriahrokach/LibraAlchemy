from mongoengine.errors import DoesNotExist
from itertools import combinations
from typing import List, Union, Dict

from database.models import Effect, Reaction
from ..utils.consts import TECHNIC_MATERIAL_LENGTH


def get_effects_by_name(name: str) -> Dict[str, str]:
    """
    Receives a name of an effect, than gets the whole effect.

    :param name: The name of the effect.
    :return: The effect.
    """
    try:
        effect = Effect.objects.get(name=name)
        return effect.json()
    except DoesNotExist:
        raise KeyError(f"Effect {name} doesn't exist.")


def get_effects_by_ingredients(materials: List[str], technic: str) -> List[Effect]:
    """
    Gets the effect from a list of ingredients.

    :param materials: the materials of the effect.
    :param technic:  the technic of the effect.

    :return: a list of the created effects.
    """
    effects: List[Effect] = []
    for materials in combinations(set(materials), TECHNIC_MATERIAL_LENGTH):
        try:
            reaction = Reaction.objects.get(
                technic=technic, materials=sorted(materials)
            )
            effects.append(Effect.objects.get(reactions=reaction))
        except DoesNotExist:
            raise KeyError(
                f'Effect with technic {technic} and materials {", ".join(materials)} does not exist.'
            )

    return effects
