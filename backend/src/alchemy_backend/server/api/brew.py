from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

from ..alchemy.brew import brew_potion
from ..alchemy.base import validate


route = APIRouter()


class PotionBrew(BaseModel):
    materials: List[str]
    technic: str


@route.post("/brew")
def api_set_potion(ingredients: PotionBrew):
    try:
        validate(ingredients.materials, ingredients.technic)
        return brew_potion(ingredients.materials, ingredients.technic)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=404, detail=str(e))
