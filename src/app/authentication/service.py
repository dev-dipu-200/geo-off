from src.models.user_model import User
from .tasks import authentication_task_test
from src.common.response import SuccessResponseModel, ErrorResponseModel, ExistingResponseModel
from src.app.authentication.schemas.auth_schema import UserSchema


async def verify_token(token: str) -> bool:
    return token == "valid_token"


async def generate_token(data: dict) -> str:
    return "valid_token" if data else "invalid_token"


async def current_user() -> str:
    return "current_user"


async def logout_user() -> str:
    return "user_logged_out"


async def login(payload=None, db=None):
    """Process the user login.
    This function simulates the process of logging in a user.
    It would typically involve validating the user credentials and generating a token.
    """
    return {"message": "Login successful"}


async def register(payload=None, db=None):
    """Process the user registration.
    This function simulates the process of registering a new user.
    It would typically involve validating the user data and saving it to the database.
    """

    if payload is None:
        return {"message": "No data provided for registration"}

    existed_user = db.query(User).filter(User.email == payload.email).first()
    if existed_user:
        return ExistingResponseModel(
            data=UserSchema.from_orm(existed_user)
        )
    if payload.password != payload.confirm_password:
        return {"message": "Passwords do not match"}
    del payload.confirm_password
    
    data = User(**payload.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return SuccessResponseModel(data=UserSchema.from_orm(data), message="Registration successful")


async def forgot_password():
    """Process the forgot password request.
    This function simulates the process of handling a forgot password request.
    It would typically involve sending a password reset email to the user."""
    return {"message": "Forgot password request processed"}


async def reset_password():
    """
    Reset the user's password.
    This function simulates the process of resetting a user's password.
    It would typically involve verifying the user's identity and updating the password in the database.
    """
    return {"message": "Password reset successful"}
