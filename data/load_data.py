import pandas as pd
from app import db as database
from app.utils import correct_date_format
from datetime import datetime
from app import models
from sqlalchemy.orm import Session
import os

db = Session(bind=database.engine)


script_dir = os.path.dirname(os.path.abspath(__file__))

def create_profile(data):
    profiles_set = set()
    for _, row in data.iterrows():
        if row['video_id'] in profiles_set:
            continue
        else:
            profiles_set.add(row['video_id'])
            profile = models.Video(
                video_id= row['video_id'],
                title= row['title'],
                channel_title= row['channel_title'],
                views= row['views'],
                tags= row['tags'],
                thumbnail_link= row['thumbnail_link'],
                description= row['description'],
                dislikes= row['dislikes'],
                category_id= row['category_id'],
                comments_disabled= row['comments_disabled'],
                ratings_disabled= row['ratings_disabled'],
                video_error_or_removed= row['video_error_or_removed'],
                comment_count= row['comment_count'],
                trending_date= correct_date_format(row['trending_date']),
                publish_time= datetime.strptime(row['publish_time'], '%Y-%m-%dT%H:%M:%S.%fZ')
            )
            db.add(profile)
            profiles_set.add(row['video_id'])
    db.commit()
    db.close()

def load_data():
    models.Base.metadata.create_all(bind=database.engine)
    data = pd.read_csv(os.path.join(script_dir, 'Invideos.csv'))
    create_profile(data)

if __name__ == "__main__":
    load_data()
