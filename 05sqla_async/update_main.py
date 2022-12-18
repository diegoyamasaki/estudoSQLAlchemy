from sqlalchemy import func # funções de agregação

from conf.helpers import formata_data
from conf.db_session import create_session

from models.sabor import Sabor

from models.picole import Picole

def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            sabor.nome = novo_nome
            session.commit()


def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        # print(picole)
        if picole:
            picole.preco = novo_preco
            picole.id_sabor = novo_sabor if novo_sabor else picole.id_sabor
            # picole.id_tipo_embalagem = 1
            # picole.id_tipo_picole =1
            session.commit()
        else:
            print(f'Não existe picole com id {id_picole}')


if __name__ == '__main__':
    # atualizar_sabor(1, 'novo_sabor')
    print('update')
    atualizar_picole(1, 9.99, 10)
