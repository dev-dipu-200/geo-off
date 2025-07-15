from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from io import BytesIO
import logging

# Suppress fontTools and weasyprint debug/info logs
logging.getLogger("fontTools").setLevel(logging.WARNING)
logging.getLogger("weasyprint").setLevel(logging.WARNING)

async def generate_pdf(data: dict, template_name: str = "test.html") -> bytes:
    """
    Generate a PDF from HTML template and input data, suppressing verbose font logs.
    """
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)
    html_content = template.render(data=data)

    pdf_io = BytesIO()
    HTML(string=html_content).write_pdf(pdf_io)

    return pdf_io.getvalue()
