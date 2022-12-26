import asyncio
from  typing import List

from sqlalchemy import func # funções de agregação
from sqlalchemy.future import select

from conf.helpers import formata_data
from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

from models.picole import Picole


async def select_todos_aditivos_nutritivos() -> None:
    async with create_session() as session:
        query = select(AditivoNutritivo)
        aditivos_nutritivos: List[AditivoNutritivo] = await session.execute(query)
        aditivos_nutritivos = aditivos_nutritivos.scalars().all()
        for aditivo in aditivos_nutritivos:
            print(aditivo.nome)
            print(formata_data(aditivo.data_criacao))


async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_session() as session:
        query = select(Sabor).where(Sabor.id == id_sabor)
        sabor: Picole = await session.execute(query)
        sabor = sabor.scalars().one_or_none()
        # sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()
        if sabor:
            print(f'NOME: {sabor.nome}')
            print(f'ID: {sabor.id}')
            print(f'DATA: {formata_data(sabor.data_criacao)}')



async def select_complexo_picole() -> None:
    async with create_session() as session:
        query = select(Picole)
        picoles: List[Picole] = await session.execute(query)
        picoles = picoles.scalars().unique().all()
        # picoles: List[Picole] = session.query(Picole).all()

        for picole in picoles:
            print(f'PREÇO: {picole.preco}')
            print(f'PREÇO: {picole.sabor}')
            print(f'ID: {picole.id}') 
            print(f'DATA: {formata_data(picole.data_criacao)}')


async def select_order_by_sabor() -> None:
    async with create_session() as session:
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        sabores: List[Sabor] = await session.execute(query)
        sabores = sabores.scalars().all()

        for sabor in sabores:
            print(f'ID: {sabor.id}') 
            print(f'Nome: {sabor.nome}')


async def select_group_by_picole() -> None:
    async with create_session() as session:
        query = select(Picole).join(Sabor).group_by(Picole.id, Picole.id_tipo_picole)
        picoles: List[Picole] = await session.execute(query)
        picoles = picoles.scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'ID: {picole.preco}')

async def select_limit() -> None:
    async with create_session() as session:
        query = select(Sabor).limit(25)
        resultado = await session.execute(query)
        sabores: List[Sabor] = resultado.scalars().unique().all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'None: {sabor.nome}')


async def select_count_revendedor() -> None:
    async with create_session() as session:
        query = select(func.count(Revendedor.id)).select_from(Revendedor)
        
        resultado = await session.execute(query)
        quantidade: int = resultado.scalar_one()
        # quantidade: int = session.query(Revendedor).count()

        print(f'Quantidade de revendedores = {quantidade}')


async def select_agregacao() -> None:
    async with create_session() as session:
        query = select(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('minimo'),
            func.max(Picole.preco).label('maximo'))
        response = await session.execute(query)
        resultado = response.all()
        print(resultado)

        print(f'Soma {resultado[0][0]}')
        print(f'Media {resultado[0][1]}')
        print(f'Minimo {resultado[0][2]}')
        print(f'Maximo {resultado[0][3]}')

if __name__ == '__main__':
    # asyncio.run(select_todos_aditivos_nutritivos())
    # asyncio.run(select_filtro_sabor(1))
    # asyncio.run(select_complexo_picole())
    # asyncio.run(select_order_by_sabor())
    # asyncio.run(select_group_by_picole())
    # asyncio.run(select_limit())
    # asyncio.run(select_count_revendedor())
    asyncio.run(select_agregacao())
    
