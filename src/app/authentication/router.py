from fastapi import APIRouter, Depends
from src.app.authentication.dependencies import get_current_user
from src.configuration.env_settings import setting
from src.app.authentication import service as auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login")
async def login():
    return await auth_service.login()


@router.post("/register")
async def register():
    return await auth_service.register()


@router.post("/logout")
async def logout():
    return await auth_service.logout()


@router.post("/forgot-password")
async def forgot_password():
    return await auth_service.forgot_password()

@router.post("/reset-password")
async def reset_password():
    return await auth_service.reset_password()

