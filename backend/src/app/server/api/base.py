from fastapi import APIRouter

from ..alchemy.base import get_technics, get_materials

route = APIRouter()


@route.get('/technics')
def api_get_technics():
    return get_technics()


@route.get('/materials')
def api_get_materials():
    return get_materials()
