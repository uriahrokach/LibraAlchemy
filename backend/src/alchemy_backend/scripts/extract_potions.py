import mongoengine as db
from alchemy_backend.database.models import Potion
import click
import os
import pandas as pd

COLUMNS = ["name", "description", "effects"]
POTION_SHEET = "potions"


def convert_potion_to_list(potion: Potion):
    effects = ", ".join(potion.json().get("effects"))
    return [potion.name, potion.description, effects]


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
    default="potions.xslx",
    help="The file to save the effects to.",
)
def main(db_url, username, password, potion_file):
    """
    Extracts and saves all current potions to an excel file.
    """
    db.connect(host=db_url, username=username, password=password)
    click.echo("Extracting all potions...")
    potions = Potion.objects.all()
    potions_as_list = [convert_potion_to_list(potion) for potion in potions]
    click.echo("saving data...")
    data = pd.DataFrame(potions_as_list, columns=COLUMNS)
    data.to_excel(potion_file, POTION_SHEET)
    click.echo(f"Done! saved to file {potion_file}.")


if __name__ == "__main__":
    main()
