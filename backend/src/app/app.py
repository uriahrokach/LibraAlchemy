from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from server.api.base import route as base_router
from server.api.brew import route as brew_router
from server.api.effects import route as effects_router
from server.api.potion import route as potion_router
from server.utils.config import get_config
from database.utils import connect_to_db


app = FastAPI()
connect_to_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_config().server.CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base_router)
app.include_router(brew_router)
app.include_router(effects_router)
app.include_router(potion_router)


if __name__ == '__main__':
    config = get_config()
    uvicorn.run(app, host=config.server.address, port=config.server.port)