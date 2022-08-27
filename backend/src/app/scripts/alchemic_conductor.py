from typing import List
from itertools import combinations
import click
from app.database.models import Reaction, Effect, db
from mongoengine import DoesNotExist

TECHNICS = ["בישול", "ייבוש וכתישה", "התססה", "חליטה"]
connection = "mongodb://libra_alchemy-db-1:27017/alchemy_test"


@click.command()
@click.option('-m', '--materials', type=str, multiple=True)
def main(materials: List[str]):
    db.connect()
    for technic in TECHNICS:
        print(f"טכניקה: {technic}")
        for mat1, mat2 in combinations(materials, 2):
            try:
                print(Reaction.objects(technic=technic))
            except DoesNotExist:
                print(mat1, mat2, technic)
            # effect = Effect.objects.get(reactions=[reaction])
            # print(f'{mat1}, {mat2}: {effect.name}')
        print('\n')


if __name__ == '__main__':
    main()



