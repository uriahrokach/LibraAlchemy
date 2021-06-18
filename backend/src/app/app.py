from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from backend.src.app.server.api.base import route as base_router
from backend.src.app.server.api.brew import route as brew_router
from backend.src.app.server.api.effects import route as effects_router
from backend.src.app.server.api.potion import route as potion_router
from backend.src.app.database.utils import connect_to_db

app = FastAPI()
connect_to_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base_router)
app.include_router(brew_router)
app.include_router(effects_router)
app.include_router(potion_router)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)