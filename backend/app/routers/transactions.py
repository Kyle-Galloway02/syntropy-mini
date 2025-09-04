from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Customer, Transaction
from ..schemas import TransactionOut
from ..deps import get_current_user
from ..schemas import TransactionOut, TransactionCreate


router = APIRouter(prefix="/customers/{customer_id}/transactions", tags=["transactions"])

@router.get("", response_model=List[TransactionOut])
def list_transactions(customer_id: int, limit: int = 20, offset: int = 0,
                      db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not db.get(Customer, customer_id):
        raise HTTPException(status_code=404, detail="customer not found")
    q = db.query(Transaction).filter(Transaction.customer_id == customer_id)\
         .order_by(Transaction.ts.desc()).limit(limit).offset(offset)
    return q.all()
@router.post("", response_model=TransactionOut)
def create_transaction(customer_id: int, payload: TransactionCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not db.get(Customer, customer_id):
        raise HTTPException(status_code=404, detail="customer not found")
    t = Transaction(customer_id=customer_id, amount=payload.amount)
    db.add(t)
    db.commit()
    db.refresh(t)
    return t
