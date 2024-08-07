from pydantic import BaseModel

class UserResponse(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True
