from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    name: str
    rating: float

class RestaurantUpdate(BaseModel):
    rating: float

class UserSignup(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str