from app.database.models import db, PotionType, Effect
from typing import List, Dict
from mongoengine import DoesNotExist
import click

import json


def create_potion_types(potion_types: Dict[str, str]):
    """
    Create potion types for effects in the DB.

    :param potion_types: The potion types to create and their data.
    """
    click.echo('Creating potion types...')
    with click.progressbar(potion_types) as potion_types_objects:
        unsaved_potion_types: List[str] = []
        for potion_type in potion_types_objects:
            try:
                effects = [Effect.objects.get(name=effect) for effect in potion_type['effects']]
                p_type = PotionType(name=potion_type['name'], effects=effects, description=potion_type['description'])
                p_type.save()
            except DoesNotExist:
                unsaved_potion_types.append(potion_type)

        click.echo(f'saved {len(potion_types) - len(unsaved_potion_types)} out of {len(potion_types)} potion types.')
        if len(unsaved_potion_types):
            click.echo(
                f'Potion types that were not saved: {", ".join(p_type["name"] for p_type in unsaved_potion_types)}.',
                err=True
            )


@click.command()
@click.option('-c', '--config-file', help='The JSON config file containing the potion types to create.')
@click.option('-u', '--db-url', default="mongodb://localhost:27017/alchemy_test",
              help="The mongodb url to save the potion types to")
def main(config_file, db_url):
    click.echo(f'Reading from file {config_file}...')
    with click.open_file(config_file, 'r', encoding='utf-8') as config_json_file:
        potion_types = config_json_file.read()
        potion_types = json.loads(potion_types)

    click.echo('Connecting to to the DB...')
    db.connect(host=db_url)

    create_potion_types(potion_types)


if __name__ == '__main__':
    main()
