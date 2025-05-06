"""
This module contains a function to fix the date format returned by the Geoex API.
"""
from datetime import timedelta
from dateutil import parser

def fix_geoex_returned_date(
    data: str | None
    ) -> str:
    """
    Fix the date format returned by Geoex API.
    The API returns dates in the format "YYYY-MM-DDTHH:MM:SSZ",
    and this function converts it to "dd/mm/yyyy hh:mm:ss".
    It also handles the timezone offset.

    Args:
        data (str): Date string in "YYYY-MM-DDTHH:MM:SSZ" format.

    Returns:
        str: formatted date string in "dd/mm/yyyy hh:mm:ss" format.
    """
    if data is None:
        return None

    fixed_date = parser.isoparse(data)
    fixed_date = fixed_date + timedelta(hours=-3)  # Adjust for timezone offset
    return fixed_date.strftime("%d/%m/%Y %H:%M:%S")
