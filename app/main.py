from fastapi import FastAPI
from . import models
from . import db as database
from .routes import videosRouter

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


app.include_router(videosRouter.router, prefix="/videos", tags=["videos"])