from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class InteractionCreate(BaseModel):
    user_id: int
    query: str
    response: str

class InteractionResponse(BaseModel):
    id: int
    user_id: int
    query: str
    response: str

    class Config:
        orm_mode = True