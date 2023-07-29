from typing import Dict, List, Union
from app.database.models import db, Effect, Potion
from mongoengine.errors import DoesNotExist, ValidationError
from pprint import pprint

import pandas as pd
import click
import os


def convert_excel_to_dict(filename: str) -> List[Dict[str, str]]:
    """
    Converts an excel sheet to file.

    :param filename: The name of the excel file.
    :return: The data as a dictionary.
    """
    xls = pd.ExcelFile(filename)
    data = xls.parse(xls.sheet_names[0])
    potions = []
    for row in data.iterrows():
        new_potion = {
            "name": row[1]["שם"],
            "description": row[1]["תיאור"],
            "effects": row[1]["אפקטים"].split(", "),
        }
        potions.append(new_potion)
    return potions


def convert_effects(effects: List[str]) -> List[Effect]:
    new_effects = []
    for name in effects:
        try:
            new_effects.append(Effect.objects.get(name=name))
        except DoesNotExist:
            print(f'Effect "{name}" does not exist (for some reason).')
            raise
    return new_effects


def insert_potions(potions: List[Dict[str, Union[str, List]]]):
    """
    Inserts all potions to the DB.

    :param potions: A dictionary of potions.
    """
    for potion_data in potions:
        try:
            potion = Potion(
                name=potion_data.get("name"),
                description=potion_data.get("description"),
                effects=convert_effects(potion_data.get("effects")),
            )
            potion.save()
            print(f'saved potion {potion_data.get("name")}')
        except DoesNotExist:
            print(f'Error saving potion: {potion_data.get("name")}')
        except ValidationError as e:
            print(f'cannot save potion {potion_data.get("name")}: {e.args}')


@click.command()
@click.option(
    "-d",
    "--db-url",
    default="mongodb://localhost:27017/alchemy_test",
    help="The mongodb url to use",
)
@click.option(
    "-u",
    "--username",
    default=os.environ.get("MONGO_USERNAME"),
    help="The mongodb username to use",
)
@click.option(
    "-p",
    "--password",
    default=os.environ.get("MONGO_PASSWORD"),
    help="The mongodb password to use",
)
@click.option(
    "-f",
    "--potion-file",
    default="potions.xlsx",
    help="The file to save the effects to.",
)
def main(db_url, username, password, potion_file):
    db.connect(host=db_url, username=username, password=password)
    click.echo("Extracting all potions from file...")
    potions = convert_excel_to_dict(potion_file)
    pprint(potions)
    click.echo("saving data to db...")
    insert_potions(potions)
    click.echo(f"Done!")


if __name__ == "__main__":
    main()
