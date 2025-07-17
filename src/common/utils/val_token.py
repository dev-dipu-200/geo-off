from jose import jwt, JWTError
from src.configuration.env_settings import setting
from datetime import datetime, timedelta, timezone

JWT_SECRET = setting.SECRET_KEY
JWT_ALGORITHM = setting.JWT_ALGORITHM
JWT_EXPIRATION_MINUTES = setting.JWT_EXPIRATION

async def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        exp = decoded_token.get("exp")
        sub = decoded_token.get("sub")
        if exp is None or sub is None:
            return None
        exp_datetime = datetime.fromtimestamp(exp, tz=timezone.utc)
        current_time = datetime.now(tz=timezone.utc)

        if exp_datetime >= current_time:
            return sub
        else:
            return None
    except JWTError:
        return None
    

async def encode_token(data: dict):
    try:
        to_encode = data.copy()
        expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
        to_encode.update({"exp": expiration, "iat": datetime.utcnow()})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
    except Exception as e:
        return f"Error encoding token: {str(e)}"