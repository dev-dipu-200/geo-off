import csv
from io import StringIO, BytesIO
from typing import List, Dict

async def generate_csv(header: List[str], data: List[Dict], filename: str = "data.csv") -> BytesIO:
    """
    Asynchronously generate a CSV file as a BytesIO stream with capitalized headers.
    Returns:
        BytesIO: The CSV content as a BytesIO stream.
    """
    
    header_map = {key: key.capitalize() for key in header}

    string_buffer = StringIO()
    writer = csv.DictWriter(string_buffer, fieldnames=header_map.values())
    writer.writeheader()

    for row in data:
        formatted_row = {header_map[key]: row.get(key, "") for key in header}
        writer.writerow(formatted_row)

    byte_buffer = BytesIO()
    byte_buffer.write(string_buffer.getvalue().encode("utf-8"))
    byte_buffer.seek(0)
    return byte_buffer
