import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class TipoEmbalagem(ModelBase):
    __tablename__ : str = 'tipos_embalagem'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<TipoEmbalagem: {self.nome}>"
