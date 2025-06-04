from pydantic import BaseModel


class scUser(BaseModel):
    login: str
    hashed_password: str

