import sqlalchemy as sa
import sqlalchemy.orm as orm

from typing import List
from datetime import datetime

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

# Nota Fiscal pode ter varios lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id')),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'))
)


class NotaFiscal(ModelBase):
    __tablename__ : str = 'notas_fiscais'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    numero_serie: str = sa.Column(sa.String(45), unique=True, nullable=True)
    descricao: str = sa.Column(sa.String(200), nullable=True)

    id_revendedor: int = sa.Column(sa.Integer, sa.ForeignKey('revendedores.id', ondelete="CASCADE"))
    revendedor: Revendedor = orm.relationship('Revendedor', lazy='joined', cascade='delete')

    # Uma nota fiscal pode ter varios lotes e um lote está ligado a uma nota fiscal
    lotes: List[Lote] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')

    def __repr__(self) -> str:
        return f"<NotaFiscal: {self.numero_serie}>"
