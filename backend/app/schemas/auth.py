from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    role: str
    phone: str | None = None
    email: str | None = None
    status: int

    model_config = ConfigDict(from_attributes=True)