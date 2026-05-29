from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        from_attributes = True



class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True