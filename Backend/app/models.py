from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=3)
    password: str = Field(..., min_length=8)  # plain for demo only


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
