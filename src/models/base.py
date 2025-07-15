from src.configuration.sql_config import Base
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), nullable=True, default=datetime.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=datetime.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


Model = BaseModel