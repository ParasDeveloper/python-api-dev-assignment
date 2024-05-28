from fastapi import FastAPI
from . import models
from . import db as database
from .routes import videosRouter
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


app.include_router(videosRouter.router, prefix="/videos", tags=["videos"])