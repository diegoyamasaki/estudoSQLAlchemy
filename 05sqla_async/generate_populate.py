import asyncio

from tqdm import tqdm
from faker import Faker
from random import random, randint, uniform
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

def populate_notas_fiscais(session: Session) -> None:
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())
    def generate_lote(lote_id):
        id_tipo_picole: int = i + 1
        quantidade: int = randint(1, 9999)
        lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
        return lote

    for i in tqdm(range(100), colour='#70FF00'):
        valor: float = uniform(100.0, 10000.0)
        numero_serie: int = i
        descricao: str = __fake.unique.paragraph(nb_sentences=2)
        nf: NotaFiscal = NotaFiscal(
            valor=valor,
            numero_serie=numero_serie,
            descricao=descricao,
            id_revendedor=i
            )
        nf.lotes.append(generate_lote(i))
        session.add(nf)

def populate_picoles(session: Session) -> None:
    __fake = Faker('pt_BR')
    __fake.unique.clear()
    __fake.seed_instance(random())

    def generate_ingredientes():
        nome: str = f'{__fake.unique.first_name().lower()} {randint(0,100000)}'
        ingrediente: Ingrediente = Ingrediente(nome=nome)
        return ingrediente

    def generate_conservante():
        nome: str = f'{__fake.unique.last_name().lower()} {randint(0,100000)}'
        descricao: str = __fake.unique.last_name().lower()
        conservante: Conservante = Conservante(nome=nome, descricao=descricao)
        return conservante
    
    def generate_aditivo_nutritivo():
        nome: str = f"{__fake.unique.color()} {randint(0,100000)}"
        __fake.unique.clear()
        formula_quimica = __fake.unique.color()
        __fake.unique.clear()
        an = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
        return an
        
    for i in tqdm(range(100), colour='#B1B8B7'):
        preco: float = uniform(1.0, 10.0)
        picole: Picole = Picole(
            preco=preco,
            id_sabor=i,
            id_tipo_picole=i,
            id_tipo_embalagem=i
            )
        picole.ingredientes.append(generate_ingredientes())
        picole.ingredientes.append(generate_ingredientes())
        picole.conservantes.append(generate_conservante())
        picole.aditivos_nutritivos.append(generate_aditivo_nutritivo())
        session.add(picole)

async def populate():
    async with create_session() as session:
        print('Init proccess...')
        populate_aditivo_nutritivo(session)
        populate_sabor(session)
        populate_tipos_embalagem(session)
        populate_tipo_picole(session)
        populate_ingredientes(session)
        populate_conservantes(session)
        populate_revendedor(session)
        # populate_lote(session)
        populate_notas_fiscais(session)
        populate_picoles(session)
        await session.commit()
        print('Finalizado com sucesso.')

if __name__ == '__main__':
    asyncio.run(create_tables()) 
    asyncio.run(populate()) 