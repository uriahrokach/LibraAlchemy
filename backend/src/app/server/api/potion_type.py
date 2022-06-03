from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

from ..alchemy.potion_types import get_type_by_name, get_types_by_effects, get_types_names, get_types_by_potion


route = APIRouter()


class GetPotionTypeByEffects(BaseModel):
    effects: List[str]


@route.get('/potion-type')
def api_get_potion_types():
    return get_types_names()


@route.get('/potion-type/{name}')
def api_get_potion_type_by_name(name: str):
    try:
        return get_type_by_name(name)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@route.post('/brew/potion-type')
def api_get_potion_type_by_effects(effects: GetPotionTypeByEffects):
    try:
        return get_types_by_effects(effects.effects)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@route.get('/potion-type/potion/{name}')
def api_get_potion_type_by_potion(name: str):
    try:
        return get_types_by_potion(name)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
