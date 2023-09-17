from typing import Optional
import os

from tempfile import NamedTemporaryFile, mkstemp
from fastapi import APIRouter
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask

from ..alchemy.potion import get_potions_by_name_regex
from ..alchemy.file_utils import save_potions_to_excel

route = APIRouter()

EXCEL_SUFFIX = '.xls'


@route.get("/download/potions")
def get_potion_sheet(regex: Optional[str] = "") -> FileResponse:
    """
    Download the potion list as an Excel sheet.
    :return: The Excel sheet containing the potion list.
    """
    potions = get_potions_by_name_regex(regex)
    _, excel_file = mkstemp(suffix=EXCEL_SUFFIX)
    save_potions_to_excel(potions, excel_file)
    return FileResponse(excel_file, background=BackgroundTask(os.remove, excel_file))

