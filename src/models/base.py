from src.configuration.sql_config import Base
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declared_attr


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


Model = BaseModel