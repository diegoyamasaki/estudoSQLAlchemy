from typing import Optional

from sqlalchemy import func # funções de agregação

from conf.db_session import create_session

from models.revendedor import Revendedor

from models.picole import Picole


def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f'Não eonctrei o picole com id {id_picole}')


def select_filtro_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'RAZAO SOCIAL: {revendedor.razao_social}')
        else:
            print(f'Não encontrado revendedor com id  {id_revendedor}')


def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Não encontrado revendedor com id  {id_revendedor}')

if __name__ == '__main__':
    # deletar_picole(1)
    select_filtro_revendedor(2)
    deletar_revendedor(2)
    
