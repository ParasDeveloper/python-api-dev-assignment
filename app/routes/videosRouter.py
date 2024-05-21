from .. import schemas, db as database
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session
from ..controllers import videosController
from typing import List, Optional, Dict

router = APIRouter()

@router.get("", response_model=None)  # Specify the correct response model
async def read_video(request: Request,db: Session = Depends(database.get_db)):
    query_params: Dict[str, str] = dict(request.query_params)
    
    video = videosController.get_video(db=db, query_params=query_params)

    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video
