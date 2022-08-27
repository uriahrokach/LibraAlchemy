from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

from ..alchemy.potion import set_potion, get_potions_by_name_regex, get_potion_by_name, delete_potion, \
    validate_str_field, get_potions_by_type
from ..alchemy.base import validate

route = APIRouter()


class PotionSet(BaseModel):
    name: str
    materials: List[str]
    technic: str
    description: str


@route.put('/potion', status_code=201)
def api_set_potion(potion: PotionSet):
    try:
        validate(potion.materials, potion.technic)
        validate_str_field(potion.name, 'Potion name')
        validate_str_field(potion.description, 'Potion Description')
        set_potion(potion.name, potion.materials, potion.technic, potion.description)
        return f'Potion {potion.name} was created successfully.'
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=404, detail=str(e))


@route.get('/potion')
def api_get_potions_by_name_regex(regex: Optional[str] = ''):
    return get_potions_by_name_regex(regex)


@route.get('/potion/{name}')
def api_get_potion_by_name(name: str):
    try:
        return get_potion_by_name(name)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@route.delete('/potion/{name}')
def api_delete_potion(name: str):
    try:
        delete_potion(name)
        return f'Potion {name} was deleted successfully.'
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@route.get('/potion/potion-type/{name}')
def api_get_potions_by_type(name: str):
    try:
        return get_potions_by_type(name)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
