from pydantic import BaseModel
from typing import Optional


class UserInSchema(BaseModel):
    username: str
    password: Optional[str] = None
    display_name: Optional[str] = None
    password_hash: Optional[str] = None
