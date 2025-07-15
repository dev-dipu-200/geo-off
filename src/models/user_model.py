from src.configuration.sql_config import Base
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    confirm_password = Column(String)

    def __init__(self, email: str, password: str, confirm_password: str):
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
