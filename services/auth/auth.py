from datetime import datetime, timedelta

import jwt
from config import cnf
from services.exceptions import APIException
from passlib.context import CryptContext
from pydantic import EmailStr
from services.profile.app.dao import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=30)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(
        to_encode, cnf.app.HASHING_KEY, cnf.app.HASHING_ALGORITHM
    )
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UserDAO.get_object(email=email)
    user_password = user.hashed_password if user != None else None
    if not user or not verify_password(password, user_password):
        raise APIException.FORBIDDEN
    return user