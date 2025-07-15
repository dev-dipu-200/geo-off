from fastapi import APIRouter, Depends
from src.app.authentication import service as auth_service
from src.app.authentication.schemas.auth_schema import AuthSchema, RegisterSchema, ResetPasswordSchema
from src.common.response import ResponseModel
from src.configuration.sql_config import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login")
async def login(payload: AuthSchema, db=Depends(get_db)):
    response = await auth_service.login(payload=payload, db=db)
    return ResponseModel(
        message="Login successful",
        data=response
    )


@router.post("/register")
async def register(payload: RegisterSchema, db=Depends(get_db)):
    response = await auth_service.register(payload=payload, db=db)
    return ResponseModel(
        result=response
    )


@router.post("/logout")
async def logout():
    response = await auth_service.logout()
    return ResponseModel(
        message="Logout successful",
        data=response
    )


@router.post("/forgot-password")
async def forgot_password():
    response = await auth_service.forgot_password()
    return ResponseModel(
        message="Forgot password request processed",
        data=response
    )

@router.post("/reset-password")
async def reset_password():
    response = await auth_service.reset_password()
    return ResponseModel(
        message="Password reset successful",
        data=response
    )

