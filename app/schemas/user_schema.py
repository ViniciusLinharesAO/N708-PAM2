from pydantic import BaseModel, EmailStr, constr


class UserCreateSchema(BaseModel):
    username: constr(min_length=3) # type: ignore
    email: EmailStr
    password: constr(min_length=6) # type: ignore

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
