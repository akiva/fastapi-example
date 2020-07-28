from functools import lru_cache
from fastapi import FastAPI
from .notes.router import router as notes_router
from .ping.router import router as ping_router
from .database import models
from .database.database import database, SessionLocal, engine
from .config.settings import Settings

models.Base.metadata.create_all(bind=engine)

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.version,
)

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(ping_router)
app.include_router(
    notes_router,
    prefix='/notes',
    tags=['notes']
)

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)
