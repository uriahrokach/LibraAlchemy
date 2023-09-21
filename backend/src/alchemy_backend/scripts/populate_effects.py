import pandas as pd
from argparse import ArgumentParser
from typing import List
from mongoengine.errors import ValidationError, DoesNotExist
from alchemy_backend.database.models import Effect, Reaction, db
import csv

TECHNICS = ["בישול", "ייבוש וכתישה", "התססה", "חליטה", "שריפה", "סחיטה"]


def populate_db(config_file, technics):
    """
    Populates the database according to the app configuration, and updates them accordingly.

    :param config_file: The configuration file
    :param technics: The technics for the
    """
    print(f"parsing data for technics {technics}...")
    tables = _parse_csv_to_tables(config_file, technics)
    print("populating db...")
    materials = _convert_table_to_db(tables)
    print("Done!")
    print(f"materials: {materials}")


def _parse_csv_to_tables(tables_file: str, header_list: List[str]):
    """
    Creates a table for each technic which contains all elements.

    :param header_list: The list of headers in the csv file
    :param tables_file: The new file of the table.
    """
    with open(tables_file, "r", encoding="utf-8") as csv_file:
        headers = {}
        reader = csv.reader(csv_file)
        for index, line in enumerate(reader):
            if line[0] in header_list:
                headers.update({index: line[0]})

    df = pd.read_csv(tables_file, header=None)
    groups = df[0].isin(list(headers.values())).cumsum()
    tables = {g.iloc[0, 0]: g.iloc[1:] for k, g in df.groupby(groups)}

    for t in tables:
        header = tables[t].iloc[0]
        tables[t] = tables[t][1:]
        tables[t].columns = header
        tables[t].set_index("material", inplace=True)
        tables[t].dropna(inplace=True, how="all")
        tables[t].fillna("", inplace=True)

    return tables


def _resolve_effect_per_reaction(effect: str, reaction: Reaction) -> Effect:
    """
    Resolves an effect per a given reaction.

    :param effect: The name of the effect to resolve.
    :param reaction: The name of the reaction to add to the effect.

    :return: The Effect that was saved.
    """
    try:
        effect = Effect.objects.get(name=effect)
    except DoesNotExist:
        effect = Effect(name=effect)

    effect.reactions.append(reaction)
    effect.save()

    return effect


def _convert_table_to_db(tables: dict):
    """
    Converts a dictionary of alchemy tables to the database schema.

    :param tables: A dictionary of tables containing the effects
    :return: The technics and materials used.
    """
    materials, technics = [], []
    for technic in tables:
        for mat1 in tables[technic]:
            if mat1 not in materials:
                materials.append(mat1)
            for mat2 in tables[technic]:
                try:
                    effect_string = tables[technic][mat1][mat2]
                    print(effect_string)
                    if effect_string != "":
                        reaction = Reaction(materials=[mat1, mat2], technic=technic)
                        reaction.save()
                        effect = _resolve_effect_per_reaction(effect_string, reaction)
                        print(
                            f"Saved effect {effect.name}, materials: {mat1}, {mat2}, technic: {technic} "
                        )
                except KeyError as e:
                    print(f"ignoring missing key in {technic} - {e}")
                except ValidationError as e:
                    print(f"Ignoring Validation error for {technic} - {e}")
    return materials


def get_parser():
    """
    Creates an argument parser to populate the DB from command line.

    :return: the argument parser.
    """
    parser = ArgumentParser(
        description="Populates the mongodb according to an alchemy csv file."
    )
    parser.add_argument(
        "-f", "--file", type=str, required=True, help="CSV file to parse."
    )
    parser.add_argument(
        "-d", "--db-url", type=str, required=True, help="The mongodb url"
    )
    parser.add_argument(
        "-u", "--username", type=str, default="", help="The mongodb username"
    )
    parser.add_argument(
        "-p", "--password", type=str, default="", help="The mongodb password"
    )

    return parser


def main():
    """
    Populates the effect DB collection.
    """
    parser = get_parser()
    args = parser.parse_args()
    db.connect(host=args.db_url, username=args.username, password=args.password)
    populate_db(args.file, TECHNICS)


if __name__ == "__main__":
    main()
