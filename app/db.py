from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from . import models 
from sqlalchemy.pool import NullPool


DATABASE_URL = "sqlite:///C:\\dev\\youtube-trending\\data\\youtube_data.db"
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False},
    poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()

# Function to test the database connection
def test_db_connection():
    print(models)
    try:
        db = get_db()
        count = db.query(models.Video).count();
        print("connected")
        print(f"Number of rows in youtube_videos table: {count}")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()
