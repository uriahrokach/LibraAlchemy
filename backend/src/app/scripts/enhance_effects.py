from app.database.models import db, Effect
from typing import List, Dict
from mongoengine import DoesNotExist
import click

import json


def enhance_effects(effects: Dict[str, str]):
    """
    Enhances effects in the database.

    :param effects: The names of the effects to enhance, and their description.
    """
    click.echo('Enhancing effects...')
    with click.progressbar(effects) as effect_names:
        unsaved_effects: List[str] = []
        for name in effect_names:
            try:
                effect = Effect.objects.get(name=name)
                effect.enhance = True
                effect.enhance_description = effects[name]
                effect.save()
            except DoesNotExist:
                unsaved_effects.append(name)

        click.echo(f'saved {len(effects) - len(unsaved_effects)} out of {len(effects)} effects.')
        if len(unsaved_effects):
            click.echo(f'Effect that were not saved: {", ".join(unsaved_effects)}.', err=True)


@click.command()
@click.option('-c', '--config-file', help='The JSON config file containing the effects to enhance.')
@click.option('-u', '--db-url', default="mongodb://localhost:27017/alchemy_test",
              help="The mongodb url to save the effects to")
def main(config_file, db_url):
    click.echo(f'Reading from file {config_file}...')
    with click.open_file(config_file, 'r', encoding='utf-8') as config_json_file:
        effects = config_json_file.read()
        effects = json.loads(effects)

    click.echo('Connecting to to the DB...')
    db.connect(host=db_url)

    enhance_effects(effects)


if __name__ == '__main__':
    main()
