from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante

def insert_aditivo_nutritivo() -> None:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Informe o nome do aditivo nutritivo.')
    formula_quimica: str = input('Informe a formula quimica do aditivo.')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)

        session.commit()
    
    print('Aditivo Nutritivo cadastrado com sucesso')

def insert_sabor() -> None:
    print('Cadastrando Sabor')
    nome: str = input('Informe o sabor.')
    sabor: Sabor = Sabor(nome=nome)
    with create_session() as session:
        session.add(sabor)
        session.commit()
    print('Sabor cadastrado com sucesso.')

def insert_tipos_embalagem() -> None:
    print('Cadastrando Tipo de Embalabem')
    nome: str = input('Informe o tipo de embalagem')

    te : TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(te)
        session.commit()
    
    print('Tipo de Embalabem cadastrado com sucesso.')

def insert_tipo_picole() -> None:
    print('Cadastrado de Tipo de Picole')
    nome: str = input('Informe o tipo de picole')
    tp: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tp)
        session.commit()
    print('Tipo Picole cadastado com sucesso.')


def insert_ingrediente() -> None:
    print('Cadastro de ingrediente')
    nome: str = input('Informe o ingrendiente')
    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()
    print('Ingrediente cadastrado com sucesso')

def insert_conservante() -> None:
    print('Cadastrado de conservante')
    nome: str = input('Informe o conservante')
    descricao: str = input('Informe a descrição')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()
    print('Conservante cadastrado com sucesso.')

if __name__ == '__main__':
    # insert_aditivo_nutritivo()
    # insert_sabor()
    # insert_tipos_embalagem()
    # insert_tipo_picole()
    # insert_ingrediente()
    insert_conservante()
