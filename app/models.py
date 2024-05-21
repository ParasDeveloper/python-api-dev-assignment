from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Video(Base):
    __tablename__ = 'youtube_videos'
    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String)
    title = Column(String)
    channel_title = Column(String)
    views = Column(Integer)
    tags = Column(String)
    thumbnail_link = Column(String)
    description = Column(String)
    likes = Column(Integer)
    dislikes = Column(Integer)
    comment_count = Column(Integer)
    trending_date = Column(DateTime)
    publish_time = Column(DateTime)
    category_id = Column(String)
    comments_disabled = Column(String)
    ratings_disabled = Column(String)
    video_error_or_removed = Column(String)
    __table_args__ = (UniqueConstraint('video_id', name='uix_video_id'),)
