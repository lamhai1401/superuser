from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.models import User, User_Pydantic
from typing import Optional
from jose import JWTError
from functools import wraps
from passlib.context import CryptContext
from datetime import datetime, timedelta
from src.configs.env import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from src.api.errors import http_error


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password: str, password_hash: str):
    return pwd_context.verify(plain_password, password_hash)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_user(username: str):
    return await User_Pydantic.from_queryset_single(User.get(username=username))


async def verify_token(token: str):
    try:
        payload: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return "Username {} is invalid".format(username)
        user = await get_user(username)
        if user is None:
            raise await http_error.Error404("Username {} is invalid".format(username))
    except JWTError as jw:
        raise await http_error.Error401(str(jw))
    except Exception as ex:
        raise await http_error.Error404(str(ex))
