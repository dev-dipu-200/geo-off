from pyclbr import Class
from pydantic import BaseModel, EmailStr, Field


class AuthSchema(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(
        default="xyz@yopmail.com",
        min_length=8,
        description="User's password with a minimum length of 8 characters",
    )
    remember_me: bool = Field(
        default=False, description="Flag to remember the user for future sessions"
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
