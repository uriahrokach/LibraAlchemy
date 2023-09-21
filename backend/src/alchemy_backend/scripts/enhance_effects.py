from alchemy_backend.database.models import db, Effect
from typing import List, Dict
from mongoengine import DoesNotExist
import click

import json


def enhance_effects(effects: Dict[str, str]):
    """
    Enhances effects in the database.

    :param effects: The names of the effects to enhance, and their description.
    """
    click.echo("Enhancing effects...")
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

        click.echo(
            f"saved {len(effects) - len(unsaved_effects)} out of {len(effects)} effects."
        )
        if len(unsaved_effects):
            click.echo(
                f'Effect that were not saved: {", ".join(unsaved_effects)}.', err=True
            )


@click.command()
@click.option(
    "-f",
    "--config-file",
    help="The JSON config file containing the effects to enhance.",
)
@click.option(
    "-d",
    "--db-url",
    default="mongodb://localhost:27017/alchemy_test",
    help="The mongodb url to save the effects to",
)
@click.option("-u", "--username", default="", help="The mongodb username")
@click.option("-p", "--password", default="", help="The mongodb password")
def main(config_file, db_url, username, password):
    click.echo(f"Reading from file {config_file}...")
    with click.open_file(config_file, "r", encoding="utf-8") as config_json_file:
        effects = config_json_file.read()
        effects = json.loads(effects)

    click.echo("Connecting to to the DB...")
    db.connect(host=db_url, username=username, password=password)

    enhance_effects(effects)


if __name__ == "__main__":
    main()
