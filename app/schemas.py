from pydantic import BaseModel
from datetime import datetime

class VideoBase(BaseModel):
    video_id : str
    title : str
    channel_title : str
    views: int
    tags : str
    thumbnail_link : str
    description : str
    likes: int
    dislikes: int
    comment_count : int
    trending_date : datetime
    publish_time : datetime
    category_id : str
    comments_disabled : str
    ratings_disabled : str
    video_error_or_removed : str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True
