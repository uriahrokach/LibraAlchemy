from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from server.api.base import route as base_router
from server.api.brew import route as brew_router
from server.api.effects import route as effects_router
from server.api.potion import route as potion_router
from server.api.potion_type import route as potion_type_router
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
app.include_router(potion_type_router)


if __name__ == "__main__":
    print(get_config().server.address, get_config().server.port)
    uvicorn.run(app, host=get_config().server.address, port=get_config().server.port)
