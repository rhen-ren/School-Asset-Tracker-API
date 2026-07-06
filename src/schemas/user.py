from pydantic import BaseModel

class LoginUser(BaseModel):
    email: str
    password: str

class GetUser(BaseModel):
    name: str
    email: str
    role: str

class SignupUser(LoginUser):
    name: str
    role: str
