import asyncio

from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

#insert parte 2

from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole

async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input('Informe o nome do aditivo nutritivo.')
    formula_quimica: str = input('Informe a formula quimica do aditivo.')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    async with create_session() as session:
        session.add(an)
        await session.commit()
        print('Aditivo Nutritivo cadastrado com sucesso')
        return an

async def insert_sabor() -> None:
    print('Cadastrando Sabor')
    nome: str = input('Informe o sabor.')
    sabor: Sabor = Sabor(nome=nome)
    async with create_session() as session:
        session.add(sabor)
        await session.commit()
    print('Sabor cadastrado com sucesso.')

async def insert_tipos_embalagem() -> None:
    print('Cadastrando Tipo de Embalabem')
    nome: str = input('Informe o tipo de embalagem')

    te : TipoEmbalagem = TipoEmbalagem(nome=nome)

    async with create_session() as session:
        session.add(te)
        await session.commit()
    
    print('Tipo de Embalabem cadastrado com sucesso.')

async def insert_tipo_picole() -> None:
    print('Cadastrado de Tipo de Picole')
    nome: str = input('Informe o tipo de picole')
    tp: TipoPicole = TipoPicole(nome=nome)

    async with create_session() as session:
        session.add(tp)
        await session.commit()
    print('Tipo Picole cadastado com sucesso.')


async def insert_ingrediente() -> Ingrediente:
    print('Cadastro de ingrediente')
    nome: str = input('Informe o ingrendiente')
    ingrediente: Ingrediente = Ingrediente(nome=nome)

    async with create_session() as session:
        session.add(ingrediente)
        await session.commit()
    print('Ingrediente cadastrado com sucesso')
    return ingrediente

async def insert_conservante() -> Conservante:
    print('Cadastrado de conservante')
    nome: str = input('Informe o conservante')
    descricao: str = input('Informe a descri????o')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    async with create_session() as session:
        session.add(conservante)
        await session.commit()
    print('Conservante cadastrado com sucesso.')
    return conservante

async def insert_revendedor() -> Revendedor:
    print('Cadastro do revendedor')
    cnpj: str = input('Informe o cnpj do revendedor')
    razao_social: str = input('Informe a raz??o socila')
    contato: str = input('Informe o contato')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    async with create_session() as session:
        session.add(revendedor)
        await session.commit()
    
    print('Revendedor cadastrado com sucesso.')
    return revendedor

async def insert_lote() -> Lote:
    print('Cadastro do lote.')
    id_tipo_picole: int = input('Informe o ID do tipo de picole')
    quantidade: int = input('Informe a quantidade')

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    async with create_session() as session:
        session.add(lote)
        await session.commit()
    
    print('Lote cadastrado com sucesso.')
    return lote


async def insert_nota_fiscal() -> None:
    print('Cadastro de Nota Fiscal.')
    valor: float = input('Informe o valor da nota fiscal.')
    numero_serie: str = input('Informe o N??mero de serie.')
    descricao: str = input('Informe a descri????o.')

    id_revendedor: int = input('Informe o ID do Revendedor.')

    nf: NotaFiscal = NotaFiscal(
        valor=valor,
        numero_serie=numero_serie,
        descricao=descricao,
        id_revendedor=id_revendedor
    )
    
    nf.lotes.append(insert_lote())

    nf.lotes.append(insert_lote())

    async with create_session() as session:
        session.add(nf)
        await session.commit()
        print(f'nota descri????o {nf.id}')
        print(f'revendedor {nf.revendedor.razao_social}')
    
    print('Nota Fiscal cadastrada com sucesso.')


async def insert_picole() -> None:
    print('Cadastro de Picole')
    preco: float = input('Informe o valor do Picole')
    
    id_sabor: int = input('Informe o ID do Sabor:')
    id_tipo_picole: int = input('Informe o ID do Tipo de Picole:')
    id_tipo_embalagem: int = input('Informe o ID do Tipo da Embalagem:')

    picole: Picole = Picole(
        preco=preco,
        id_sabor=id_sabor,
        id_tipo_picole=id_tipo_picole,
        id_tipo_embalagem=id_tipo_embalagem
    )

    picole.ingredientes.append(insert_ingrediente())
    picole.ingredientes.append(insert_ingrediente())
    picole.conservantes.append(insert_conservante())
    picole.aditivos_nutritivos.append(insert_aditivo_nutritivo())

    async with create_session() as session:
        session.add(picole)
        await session.commit()
        print(f'picole id {picole.id}')
        print(f'picole sabor {picole.sabor.nome}')
        print(f'picole tipo de embalagem: {picole.tipo_embalagem.nome}')
        
    
    print('Picole cadastrada com sucesso.')

if __name__ == '__main__':
    # asyncio.run(insert_aditivo_nutritivo())
    # asyncio.run(insert_sabor()) 
    # asyncio.run(insert_tipos_embalagem()) 
    # asyncio.run(insert_tipo_picole())
    # asyncio.run(insert_ingrediente())
    # asyncio.run(insert_conservante())
    # rev = asyncio.run(insert_revendedor())
    # print(f'ID revendedor {rev.id}')
    # lote = asyncio.run(insert_lote())
    # print(f'ID lote {lote.id}')
    # asyncio.run(insert_nota_fiscal())
    asyncio.run(insert_picole())
