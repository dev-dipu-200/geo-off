from fastapi import APIRouter, Depends
# from src.app.authentication.dependencies import get_current_user
# from src.configuration.env_settings import setting
from src.app.authentication import service as auth_service
from src.app.authentication.schemas.auth_schema import AuthSchema, RegisterSchema, ResetPasswordSchema
from src.configuration.sql_config import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login")
async def login():
    return await auth_service.login()


@router.post("/register")
async def register(payload: RegisterSchema, db=Depends(get_db)):
    return await auth_service.register(pyload=payload, db=db)


@router.post("/logout")
async def logout():
    return await auth_service.logout()


@router.post("/forgot-password")
async def forgot_password():
    return await auth_service.forgot_password()

@router.post("/reset-password")
async def reset_password():
    return await auth_service.reset_password()

