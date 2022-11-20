
from tqdm import tqdm
from faker import Faker
from random import random, randint
from conf.db_session import create_session, create_tables
from sqlalchemy.orm import Session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


def populate_aditivo_nutritivo(session: Session):
    __fake = Faker('pt_BR')
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#FF1493'):
        nome: str = i
        __fake.unique.clear()
        formula_quimica = __fake.unique.color()
        __fake.unique.clear()
        an = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
        
        session.add(an)

def populate_sabor(session: Session):
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#CD853F'):
        nome: str = __fake.unique.first_name().lower()
        sabor = Sabor(nome=nome)
        session.add(sabor)

def populate_tipos_embalagem(session: Session):
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#8A2BE2'):
        nome: str = __fake.unique.first_name().lower()
        te = TipoEmbalagem(nome=nome)
        session.add(te)


def populate_tipo_picole(session: Session):
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#3CB371'):
        nome: str = __fake.unique.first_name().lower()
        tp = TipoPicole(nome=nome)
        session.add(tp)

def populate_ingredientes(session: Session):
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#8B008B'):
        nome: str = __fake.unique.first_name().lower()
        ingrediente: Ingrediente = Ingrediente(nome=nome)
        session.add(ingrediente)


def populate_conservantes(session: Session):
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#C6D249'):
        __fake.unique.clear()
        nome: str = i
        __fake.unique.clear()
        descricao: str = __fake.unique.last_name().lower()
        conservante: Conservante = Conservante(nome=nome, descricao=descricao)
        session.add(conservante)

def populate_revendedor(session: Session) -> None:
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#58ADE5'):
        cnpj: str = i
        razao_social: str = __fake.unique.company()
        contato: str = __fake.unique.phone_number()
        revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)
        session.add(revendedor)

def populate_lote(session: Session) -> None:
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    for i in tqdm(range(100), colour='#FB9F22'):
        id_tipo_picole: int = i + 1
        quantidade: int = randint(1, 9999)
        lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
        session.add(lote)

def populate():
    with create_session() as session:
        print('Init proccess...')
        populate_aditivo_nutritivo(session)
        populate_sabor(session)
        populate_tipos_embalagem(session)
        populate_tipo_picole(session)
        populate_ingredientes(session)
        populate_conservantes(session)
        populate_revendedor(session)
        populate_lote(session)
        session.commit()

if __name__ == '__main__':
    create_tables()
    populate()