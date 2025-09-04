from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, EmailStr, field_serializer

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr

class CustomerOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        from_attributes = True

class TransactionOut(BaseModel):
    id: int
    amount: Decimal
    ts: datetime

    # Serialize Decimal -> float in responses
    @field_serializer('amount')
    def ser_amount(self, v: Decimal) -> float:
        return float(v)

    class Config:
        from_attributes = True

class LoginIn(BaseModel):
    username: str
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
class TransactionCreate(BaseModel):
    amount: float
