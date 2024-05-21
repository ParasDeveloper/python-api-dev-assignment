Project Installation:
    - Create virtual enviroment inside project directory `python -m venv env`
    - Activate the virtual enviroment `source env/Scripts/activate`
    - Install dependencies `pip install -r requirements.txt`
    - Create .db file `python -m data.load_data`

Run:
    - start app `uvicorn app.main:app --reload`

Folder Structure:
    YOUTUBE-TRENDING
        ├───app
        │   │   db.py
        │   │   main.py
        │   │   models.py
        │   │   schemas.py
        │   │   utils.py
        │   │   
        │   ├───controllers
        │   │      videosController.py
        │   │           
        │   └───routes
        │         videosRouter.py
        │           
        └───data
              INvideos.csv
              load_data.py
              youtube_data.db
       
    - INvideos.csv: Kaggle dataset of trending videos.
    - load_data.py: Module to read data from .csv file and generate .db file.
    - youtub_data.db: Database file generated from .csv file using load_data module.
    - db.py: connects to sqlite database and returns session object.
    - models.py: Contains models class for tables structure.
    - schema: contains Schema class for data validation.
    - utils.py: Contains utility functions.
    - videosController.py - Contains route controller functions.
    - videoRouter.py - Contains route handlers.
    - main.py - Initialize app using FastApi.