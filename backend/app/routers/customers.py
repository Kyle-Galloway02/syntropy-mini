from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Customer
from ..schemas import CustomerCreate, CustomerOut
from ..deps import get_current_user

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("", response_model=CustomerOut)
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if db.query(Customer).filter_by(email=payload.email).first():
        raise HTTPException(status_code=400, detail="email already exists")
    c = Customer(name=payload.name, email=payload.email)
    db.add(c); db.commit(); db.refresh(c)
    return c

@router.get("", response_model=List[CustomerOut])
def list_customers(q: str | None = None, limit: int = 20, offset: int = 0,
                   db: Session = Depends(get_db), user=Depends(get_current_user)):
    query = db.query(Customer)
    if q:
        query = query.filter(Customer.name.ilike(f"%{q}%"))
    return query.order_by(Customer.id.desc()).limit(limit).offset(offset).all()
