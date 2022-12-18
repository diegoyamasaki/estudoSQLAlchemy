from pathlib import Path
from typing import Optional

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from models.model_base import ModelBase

__async_engine: Optional[AsyncEngine] = None


def create_engine(sqlite: bool = False) -> AsyncEngine:
   global __async_engine
   
   if __async_engine:
    return

   if sqlite:
    arquivo_db = 'db/picoles.sqlite'
    folter = Path(arquivo_db).parent
    folter.mkdir(parents=True, exist_ok=True)

    conn_str = f'sqlite+aiosqlite:///{arquivo_db}'

    __async_engine = create_async_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False}) 
   else:
    # sem sqlite
    conn_str = f'postgres+asyncpg://root:root@localhost:5432/picoles'
    __async_engine = create_async_engine(url=conn_str, echo=False) 



def create_session() -> AsyncSession:
    global __async_engine

    if not __async_engine:
        create_async_engine()
    
    __async_session = sessionmaker(
        __async_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    session: AsyncSession = __async_session()

    return session

async def create_tables() -> None:
    global __async_engine

    if not __async_engine:
        create_async_engine()
    
    import models.__all__models
    async with __async_engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all)
        await conn.runc_async(ModelBase.metadata.create_all)
