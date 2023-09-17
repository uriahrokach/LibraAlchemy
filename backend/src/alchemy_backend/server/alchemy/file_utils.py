from typing import List
import pyexcel
import pyexcel_xls
from database.models import Potion

EFFECTS_KEY = 'effects'


def save_potions_to_excel(potions: List[Potion], file_name: str = 'potions.xslx') -> None:
    """
    Saves a list of potions to an Excel file.

    :param potions: The list of potions to save.
    :param file_name: The name of the file to save them to.
    """
    potion_data = [potion.json() for potion in potions]
    for potion_json in potion_data:
        potion_json[EFFECTS_KEY] = ', '.join(potion_json.get('effects'))
    pyexcel.save_as(records=potion_data, dest_file_name=file_name)


# def load_potions_from_file(potions_file: str) -> List[Potion]:
#     sheet = pyexcel.get_sheet(file_name=potions_file, name_columns_by_row=0)
#     for potion_data in pyexcel.get_records():
#         effects = potion_data[EFFECTS_KEY].replace(' ', '').split(',')
#
