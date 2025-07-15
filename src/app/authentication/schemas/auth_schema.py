from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from src.common.enums.role_enum import UserRole


class AuthSchema(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(
        default="xyz@yopmail.com",
        min_length=8,
        description="User's password with a minimum length of 8 characters",
    )
    remember_me: Optional[bool] = Field(
        default=None, description="Flag to remember the user for future sessions"
    )


class RegisterSchema(BaseModel):
    email: EmailStr = Field(
        default="xyz@yopmail.com", description="User's email address for registration"
    )
    password: str = Field(
        default="password123",
        min_length=8,
        description="Password with a minimum length of 8 characters",
    )
    confirm_password: str = Field(
        default="password123", min_length=8, description="Confirmation of the password"
    )

    role: Optional[UserRole] = Field(default=UserRole.USER, description="Role of the user")
    is_active: Optional[bool] = Field(
        default=True, description="Flag to indicate if the user is active"
    )



class ResetPasswordSchema(BaseModel):
    email: EmailStr = Field(..., description="User's email address for password reset")
    new_password: str = Field(
        default="password123",
        min_length=8,
        description="New password with a minimum length of 8 characters",
    )
    confirm_password: str = Field(
        default="password123", min_length=8, description="Confirmation of the new password"
    )

class UserSchema(BaseModel):
    id: int
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[UserRole] = None

    class Config:
        from_attributes=True