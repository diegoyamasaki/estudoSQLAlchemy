from  typing import List

from sqlalchemy import func # funções de agregação

from conf.helpers import formata_data
from conf.db_session import create_session



from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

from models.picole import Picole


def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        aditivios_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()
        # aditivios_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        for aditivo in aditivios_nutritivos:
            print(aditivo.nome)
            print(formata_data(aditivo.data_criacao))


def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        # forma 1
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()  
        
        # forma 2 -> recomendado
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none() 
        
        # forma 3 -> Vai lançar um exception se não encontra
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()
        
        # forma 4 -> Usando where ao inves de filter pode utilizar one, one_or_none ou first para retornar os dados. 
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()
        if sabor:
            print(f'NOME: {sabor.nome}')
            print(f'ID: {sabor.id}')
            print(f'DATA: {formata_data(sabor.data_criacao)}')



def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()

        for picole in picoles:
            print(f'PREÇO: {picole.preco}')
            print(f'PREÇO: {picole.sabor}')
            print(f'ID: {picole.id}') 
            print(f'DATA: {formata_data(picole.data_criacao)}')


def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()

        for sabor in sabores:
            print(f'ID: {sabor.id}') 
            print(f'Npme: {sabor.nome}')


def select_group_by_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'ID: {picole.preco}')

def select_limit() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(25)

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'None: {sabor.nome}')


def select_count_revendedor() -> None:
    with create_session() as session:
        quantidade: int = session.query(Revendedor).count()

        print(f'Quantidade de revendedores = {quantidade}')


def select_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('minimo'),
            func.max(Picole.preco).label('maximo'),
        ).all()

        print(resultado)

        print(f'Soma {resultado[0][0]}')
        print(f'Media {resultado[0][1]}')
        print(f'Minimo {resultado[0][2]}')
        print(f'Maximo {resultado[0][3]}')

if __name__ == '__main__':
    # select_todos_aditivos_nutritivos()
    # select_filtro_sabor(99999)
    # select_complexo_picole()
    # select_order_by_sabor()
    # select_order_by_sabor()
    # select_limit()
    # select_count_revendedor()
    select_agregacao()
