"""First migration

Revision ID: da1053d0b21c
Revises: 
Create Date: 2020-02-27 01:38:42.497334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da1053d0b21c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('distrito',
    sa.Column('codigo', sa.Integer(), nullable=False, comment='Código do distrito conforme IBGE'),
    sa.Column('nome', sa.String(length=18), nullable=False, comment='Distrito municipal'),
    sa.PrimaryKeyConstraint('codigo')
    )
    op.create_table('subprefeitura',
    sa.Column('codigo', sa.Integer(), nullable=False, comment='Código da subprefeitura (2003 a 2012)'),
    sa.Column('nome', sa.String(length=25), nullable=False, comment='Nome da subprefeitura'),
    sa.PrimaryKeyConstraint('codigo')
    )
    op.create_table('feira',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='Número de identificação do estabelecimento georreferenciado por SMDU/Deinfo'),
    sa.Column('registro', sa.String(length=6), nullable=False, comment='Número do registro da feira livre na PMSP'),
    sa.Column('nome_feira', sa.String(length=30), nullable=False, comment='Denominação da feira livre atribuída pela Supervisão de Abastecimento'),
    sa.Column('setor_censitario', sa.String(length=30), nullable=False, comment='Setor censitário conforme IBGE'),
    sa.Column('area_ponderacao', sa.String(length=13), nullable=False, comment='Área de ponderação (agrupamento de setores censitários) conforme IBGE 2010'),
    sa.Column('codigo_distrito', sa.Integer(), nullable=False),
    sa.Column('codigo_subprefeitura', sa.Integer(), nullable=False),
    sa.Column('regiao5', sa.String(length=6), nullable=False, comment='Região conforme divisão do Município em 5 áreas'),
    sa.Column('regiao8', sa.String(length=7), nullable=False, comment='Região conforme divisão do Município em 8 áreas'),
    sa.Column('logradouro', sa.String(length=34), nullable=False, comment='Nome do logradouro onde se localiza a feira livre'),
    sa.Column('numero', sa.String(length=5), comment='Um número do logradouro onde se localiza a feira livre'),
    sa.Column('bairro', sa.String(length=20), nullable=False, comment='Bairro de localização da feira livre'),
    sa.Column('referencia', sa.String(length=24), comment='Ponto de referência da localização da feira livre'),
    sa.Column('latitude', sa.String(length=10), nullable=False, comment='Latitude da localização do estabelecimento no território do Município, conforme MDC'),
    sa.Column('longitude', sa.String(length=10), nullable=False, comment='Longitude da localização do estabelecimento no território do Município, conforme MDC'),
    sa.ForeignKeyConstraint(['codigo_distrito'], ['distrito.codigo'], ),
    sa.ForeignKeyConstraint(['codigo_subprefeitura'], ['subprefeitura.codigo'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('registro')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feira')
    op.drop_table('subprefeitura')
    op.drop_table('distrito')
    # ### end Alembic commands ###
