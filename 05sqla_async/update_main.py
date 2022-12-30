import asyncio

from sqlalchemy import func # funções de agregação
from sqlalchemy.future import select

from conf.helpers import formata_data
from conf.db_session import create_session

from models.sabor import Sabor

from models.picole import Picole

async def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    async with create_session() as session:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        response = await session.execute(query)
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        sabor: Sabor = response.unique().scalar_one_or_none()

        if sabor:
            sabor.nome = novo_nome
            await session.commit()


async def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    async with create_session() as session:
        query = select(Picole).filter(Picole.id == id_picole)
        response = await session.execute(query)
        # picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        picole: Picole =  response.unique().scalar_one_or_none()
        # print(picole)
        if picole:
            picole.preco = novo_preco
            picole.id_sabor = novo_sabor if novo_sabor else picole.id_sabor
            # picole.id_tipo_embalagem = 1
            # picole.id_tipo_picole =1
            await session.commit()
        else:
            print(f'Não existe picole com id {id_picole}')


if __name__ == '__main__':
    # asyncio.run(atualizar_sabor(1, 'novo_sabor'))
    
    # print('update')
    # atualizar_picole(1, 9.99, 10)
    asyncio.run(atualizar_picole(1, 9.99, 10))
