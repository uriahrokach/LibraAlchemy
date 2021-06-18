from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..alchemy.effects import get_effects_by_name

route = APIRouter()


class EffectSet(BaseModel):
    name: str


@route.get('/effect')
def api_get_effect(effect: EffectSet):
    try:
        return get_effects_by_name(effect.name)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
