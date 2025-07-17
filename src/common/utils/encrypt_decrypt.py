import os
import json
from passlib.context import CryptContext
from cryptography.fernet import Fernet
from jose import jwt
from datetime import datetime, timedelta

FERNET_SECRET_KEY = os.getenv("FERNET_SECRET_KEY") or Fernet.generate_key().decode()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class EncryptedPassword:
    fernet = Fernet(FERNET_SECRET_KEY.encode())
    @staticmethod
    def get_hash_passssword(plain_password):
        return pwd_context.hash(plain_password)

    @staticmethod
    def verify_hash_password(plain_password, hash_password):
        return pwd_context.verify(plain_password, hash_password)

    @classmethod
    def encrypt_data(cls, data: dict) -> str:
        """Encrypt dictionary to a secure string."""
        json_data = json.dumps(data)
        encrypted = cls.fernet.encrypt(json_data.encode())
        return encrypted.decode()

    @classmethod
    def decrypt_data(cls, encrypted_str: str) -> dict:
        """Decrypt encrypted string back to dictionary."""
        decrypted = cls.fernet.decrypt(encrypted_str.encode())
        return json.loads(decrypted.decode())
