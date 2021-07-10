from typing import List
from backend.src.app.server.utils.config import get_config
from backend.src.app.server.utils.consts import POTION_MATERIAL_MIN, POTION_MATERIAL_MAX

config = get_config()


def get_materials() -> List[str]:
    """
    Gets The materials of the alchemy system.

    :return: a list containing the materials of the alchemy system.
    """
    return config.alchemy.materials


def get_technics() -> List[str]:
    """
    Gets The technics of the alchemy system.

    :return: a list containing the materials of the alchemy system.
    """
    return config.alchemy.technics


def validate(materials: List[str] = None, technic: str = None) -> None:
    """
    Validates materials and technics.

    :param materials: The materials to validate.
    :param technic: The technic to validate.
    :raise ValueError: If the ingredients are not valid.
    """
    if materials is not None:
        if len(materials) > POTION_MATERIAL_MAX or len(materials) < POTION_MATERIAL_MIN:
            raise ValueError(f'Number of materials must be between {POTION_MATERIAL_MIN} and {POTION_MATERIAL_MAX}')

        for material in materials:
            if material not in config.alchemy.materials:
                raise ValueError(f'Material {material} is not a valid material')

    if technic and technic not in config.alchemy.technics:
        raise ValueError(f'Technic {technic} is not a valid technic')