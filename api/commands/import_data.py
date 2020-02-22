import csv
from pathlib import Path

import click
from flask.cli import with_appcontext

from api.extensions import db
from api.feiras_livres.models import Distrito, Subprefeitura


def csv_reader_generator(filepath):
    with open(filepath) as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row


def insert_districts(districts):
    for district in districts:
        instance = Distrito(**district)
        db.session.add(instance)


def insert_subprefectures(subprefectures):
    for subprefecture in subprefectures:
        instance = Subprefeitura(**subprefecture)
        db.session.add(instance)


@click.command()
@click.argument('filepath')
@with_appcontext
def import_data(filepath):
    print(filepath)
    absolute_filepath = str(Path(filepath).resolve())

    district_ids = set()
    subprefecture_ids = set()

    districts = []
    subprefectures = []
    street_markets = []

    for row in csv_reader_generator(absolute_filepath):
        if (coddist := int(row['CODDIST'])) not in district_ids:
            districts.append({'codigo': coddist, 'nome': row['DISTRITO']})
            district_ids.add(coddist)

        if (codsubpref := int(row['CODSUBPREF'])) not in subprefecture_ids:
            subprefectures.append({'codigo': codsubpref, 'nome': row['SUBPREFE']})
            subprefecture_ids.add(codsubpref)

        street_markets.append(row)

    insert_districts(districts)
    insert_subprefectures(subprefectures)
    db.session.commit()
