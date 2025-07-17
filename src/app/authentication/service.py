from src.models.user_model import User
from .tasks import authentication_task_test
from src.common.response import (
    SuccessResponseModel,
    ErrorResponseModel,
    ExistingResponseModel,
)
from src.app.authentication.schemas.auth_schema import UserSchema
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.common.utils.encrypt_decrypt import EncryptedPassword as data_encrypt_decrypt
from src.common.utils.val_token import encode_token, decode_token
from src.configuration.sql_config import SessionLocal
from fastapi import HTTPException, status, Depends

oauth2_scheme = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
):
    token = credentials.credentials
    try:
        decoded_token = await decode_token(token=token)
        if decoded_token:
            session = SessionLocal()
            user = session.query(User).filter(User.email == decoded_token).first()
            return UserSchema.from_orm(user)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Token {e}"
        )


async def login(payload=None, db=None):
    """Process the user login.
    This function simulates the process of logging in a user.
    It would typically involve validating the user credentials and generating a token.
    """
    if payload is None:
        return ErrorResponseModel(message="No data provided for login")
    if not payload.email or not payload.password:
        return ErrorResponseModel(message="Email and password are required")
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        return ErrorResponseModel(message="User not found")
    if not data_encrypt_decrypt.verify_hash_password(payload.password, user.password):
        return ErrorResponseModel(message="Invalid password")
    token = await encode_token(
        {"sub": user.email, "role": user.role, "user_id": user.id}
    )
    if not token:
        return ErrorResponseModel(message="Failed to generate token")
    return {
        "message": "Login successful",
        "token": token,
        "user": UserSchema.from_orm(user),
    }


async def register(payload=None, db=None):
    if payload is None:
        return {"message": "No data provided for registration"}

    existed_user = db.query(User).filter(User.email == payload.email).first()
    if existed_user:
        return ExistingResponseModel(data=UserSchema.from_orm(existed_user))
    if payload.password != payload.confirm_password:
        return {"message": "Passwords do not match"}
    if not payload.password:
        return ErrorResponseModel(message="Failed to encrypt password")
    payload.password = await data_encrypt_decrypt.get_hash_passssword(payload.password)

    del payload.confirm_password

    data = User(**payload.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return SuccessResponseModel(
        data=UserSchema.from_orm(data), message="Registration successful"
    )


async def forgot_password(payload: None, db=None):
    """
    Process the user's forgot password request.
    This function simulates the process of sending a password reset email to the user.
    """
    if payload is None:
        return ErrorResponseModel(
            message="No data provided for forgot password request"
        )

    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        return ErrorResponseModel(message="User not found")
    reset_token = await encode_token(
        {"sub": user.email, "role": user.role, "user_id": user.id}
    )
    if not reset_token:
        return ErrorResponseModel(message="Failed to generate token")
    await authentication_task_test.delay(email=user.email, token=reset_token)

    return {"message": "Forgot password request processed"}


async def reset_password(payload=None, db=None):
    """
    Reset the user's password.
    This function simulates the process of resetting a user's password.
    It would typically involve verifying the user's identity and updating the password in the database.
    """
    if payload is None:
        return ErrorResponseModel(message="No data provided for password reset")
    if payload.new_password != payload.confirm_password:
        return ErrorResponseModel(message="Passwords do not match")
    if not payload.new_password:
        return ErrorResponseModel(message="Failed to encrypt password")
    payload.new_password = await data_encrypt_decrypt.get_hash_passssword(
        payload.new_password
    )
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        return ErrorResponseModel(message="User not found")
    user.password = payload.new_password
    db.commit()
    return {"message": "Password reset successful"}
