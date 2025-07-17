from .base import Model
from sqlalchemy import Column, Integer, String

class HtmlTemplate(Model):
    __tablename__ = "html_templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False , unique=True, index=True)
    subject = Column(String, nullable=False, unique=True)
    body = Column(String, nullable=False)

