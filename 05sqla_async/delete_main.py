import asyncio

from typing import Optional

from sqlalchemy import func # funções de agregação
from sqlalchemy.future import select

from conf.db_session import create_session

from models.revendedor import Revendedor

from models.picole import Picole


async def deletar_picole(id_picole: int) -> None:
    async with create_session() as session:
        query = select(Picole).filter(Picole.id == id_picole)
        response = await session.execute(query)
        # picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        picole: Optional[Picole] = response.unique().scalar_one_or_none()

        if picole:
            await session.delete(picole)
            await session.commit()
        else:
            print(f'Não eonctrei o picole com id {id_picole}')


async def select_filtro_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        query = select(Revendedor).filter(Revendedor.id == id_revendedor)
        response = await session.execute(query)
        # revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        revendedor: Optional[Revendedor] = response.unique().scalar_one_or_none()
        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'RAZAO SOCIAL: {revendedor.razao_social}')
        else:
            print(f'Não encontrado revendedor com id  {id_revendedor}')


async def deletar_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        query = select(Revendedor).filter(Revendedor.id == id_revendedor)
        response = await session.execute(query)
        # revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        revendedor: Optional[Revendedor] = response.unique().scalar_one_or_none()
        if revendedor:
            await session.delete(revendedor)
            await session.commit()
        else:
            print(f'Não encontrado revendedor com id  {id_revendedor}')

async def busca_delete_revendedor():
    await select_filtro_revendedor(2)
    await deletar_revendedor(2)

if __name__ == '__main__':
    # asyncio.run(deletar_picole(1))
    asyncio.run(busca_delete_revendedor())    
