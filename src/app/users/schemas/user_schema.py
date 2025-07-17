from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from src.common.enums.role_enum import UserRole
from datetime import datetime as Datetime


class UserSchema(BaseModel):
    id: int
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[UserRole] = None
    created_at: Optional[Datetime] = None
    updated_at: Optional[Datetime] = None

    class Config:
        from_attributes=True