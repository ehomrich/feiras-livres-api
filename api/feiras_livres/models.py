from api.extensions import db


class Distrito(db.Model):
    codigo = db.Column(
        db.Integer,
        primary_key=True,
        comment='Código do distrito conforme IBGE'
    )
    nome = db.Column(
        db.String(18),
        nullable=False,
        comment='Distrito municipal'
    )
    feiras = db.relationship('Feira', lazy='select', backref='distrito')


class Subprefeitura(db.Model):
    codigo = db.Column(
        db.Integer,
        primary_key=True,
        comment='Código da subprefeitura (2003 a 2012)'
    )
    nome = db.Column(
        db.String(25),
        nullable=False,
        comment='Nome da subprefeitura'
    )
    feiras = db.relationship('Feira', lazy='select', backref='subprefeitura')


class Feira(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        comment='Número de identificação do estabelecimento georreferenciado por SMDU/Deinfo'
    )
    registro = db.Column(
        db.String(6),
        unique=True,
        nullable=False,
        comment='Número do registro da feira livre na PMSP'
    )
    nome_feira = db.Column(
        db.String(30),
        nullable=False,
        comment='Denominação da feira livre atribuída pela Supervisão de Abastecimento'
    )
    setor_censitario = db.Column(
        db.String(30),
        nullable=False,
        comment='Setor censitário conforme IBGE'
    )
    area_ponderacao = db.Column(
        db.String(13),
        nullable=False,
        comment='Área de ponderação (agrupamento de setores censitários) conforme IBGE 2010'
    )
    codigo_distrito = db.Column(
        db.Integer,
        db.ForeignKey('distrito.codigo'),
        nullable=False
    )
    codigo_subprefeitura = db.Column(
        db.Integer,
        db.ForeignKey('subprefeitura.codigo'),
        nullable=False
    )
    regiao5 = db.Column(
        db.String(6),
        nullable=False,
        comment='Região conforme divisão do Município em 5 áreas'
    )
    regiao8 = db.Column(
        db.String(7),
        nullable=False,
        comment='Região conforme divisão do Município em 8 áreas'
    )
    logradouro = db.Column(
        db.String(34),
        nullable=False,
        comment='Nome do logradouro onde se localiza a feira livre'
    )
    numero = db.Column(
        db.String(5),
        comment='Um número do logradouro onde se localiza a feira livre'
    )
    bairro = db.Column(
        db.String(20),
        nullable=False,
        comment='Bairro de localização da feira livre'
    )
    referencia = db.Column(
        db.String(24),
        comment='Ponto de referência da localização da feira livre'
    )
    latitude = db.Column(
        db.String(10),
        nullable=False,
        comment='Latitude da localização do estabelecimento no território do Município, conforme MDC'
    )
    longitude = db.Column(
        db.String(10),
        nullable=False,
        comment='Longitude da localização do estabelecimento no território do Município, conforme MDC'
    )
