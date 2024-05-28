from sqlalchemy.orm import Session, load_only
from .. import models
from typing import Optional, List, Dict
from sqlalchemy import inspect
from .. utils import check_if_column_exists


def get_video(
    db: Session,
    query_params:Dict[str, str] = []
):
    query = db.query(models.Video)

    page = int(query_params.get('page') or 0)
    limit = int(query_params.get('limit') or 10)
    columns = []
    if (query_params.get('columns')):
        columns = query_params.get('columns').split(',')
    

    for key,value in query_params.items():
        if(key == 'page' or key == 'limit' or key == 'columns'):
            continue
        column_exists = check_if_column_exists(model=models.Video, attribute=key)
        if column_exists is True:
            query = query.filter(getattr(models.Video, key).ilike(f'%{value}%'))


    valid_columns = []
    if columns:
        for col in columns:
            column_exists = check_if_column_exists(model=models.Video, attribute=col)
            if column_exists:
                valid_columns.append(col)

    
    if valid_columns:
        columns_to_select = [getattr(models.Video, column) for column in valid_columns]
        query = query.options(load_only(*columns_to_select))

    if page:
        query = query.offset(page*limit)
    query = query.limit(limit)
    video = query.all()

    return video