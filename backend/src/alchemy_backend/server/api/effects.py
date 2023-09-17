from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from ..alchemy.effects import get_effects_by_name, get_effects_by_ingredients
from ..alchemy.base import validate

route = APIRouter()


class EffectByIngredients(BaseModel):
    materials: List[str]
    technic: str


@route.get("/effect")
def api_get_effect(effect: str):
    try:
        return get_effects_by_name(effect)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@route.post("/effect/ingredients")
def api_get_effects_by_ingredients(request: EffectByIngredients):
    try:
        validate(request.materials, request.technic)
        effects = get_effects_by_ingredients(request.materials, request.technic)
        return [effect.json() for effect in effects]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=404, detail=str(e))
