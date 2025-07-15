from src.configuration.sql_config import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Model
from src.common.enums.role_enum import UserRole

class User(Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default=UserRole.USER)
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    otp = relationship("OTP", back_populates="user", cascade="all, delete-orphan")


class Address(Model):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    address_line_1 = Column(String, nullable=False)
    address_line_2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)

    user = relationship("User", back_populates="addresses")



class OTP(Model):
    __tablename__ = 'otp'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    otp_code = Column(String, nullable=False)
    is_verified = Column(Integer, default=0)
    user = relationship("User", back_populates="otp")


