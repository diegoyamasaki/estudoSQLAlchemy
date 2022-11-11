import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from pathlib import Path # Usado no SQLite
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase

__engine: Optional[Engine] = None

def create_engine(sqlite: bool = False):
    global __engine

    if __engine:
        return __engine
    
    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    else:
        conn_str = f'mysql://root:root@localhost:3306/picoles'
        __engine = sa.create_engine(url=conn_str, echo=False)


def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine(True) # Para criar o banco como sqlite
    
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine    

    if not __engine:
        create_engine(True)
    
    import models.__all__models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
    
    

