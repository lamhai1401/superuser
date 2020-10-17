from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    secret_key: str
