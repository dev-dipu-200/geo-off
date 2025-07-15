import csv
from io import StringIO, BytesIO
from typing import List, Dict, Any
from datetime import datetime

async def generate_csv(header: List[str], data: List[Dict[str, Any]], filename: str = "data.csv") -> BytesIO:
    """
    Asynchronously generate a CSV file as a BytesIO stream with capitalized headers
    and date-only formatting for datetime fields.

    Returns:
        BytesIO: The CSV content as a BytesIO stream.
    """

    header_map = {key: key.capitalize() for key in header}

    string_buffer = StringIO()
    writer = csv.DictWriter(string_buffer, fieldnames=header_map.values())
    writer.writeheader()

    for row in data:
        formatted_row = {}
        for key in header:
            value = row.get(key, "")
            if isinstance(value, datetime):
                value = value.strftime("%Y-%m-%d")
            formatted_row[header_map[key]] = value
        writer.writerow(formatted_row)

    byte_buffer = BytesIO()
    byte_buffer.write(string_buffer.getvalue().encode("utf-8"))
    byte_buffer.seek(0)
    return byte_buffer
