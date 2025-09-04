from decimal import Decimal
from sqlalchemy.orm import Session
from .models import Customer, Transaction

def seed_if_empty(db: Session) -> None:
    # Only seed if there are no customers yet
    if db.query(Customer).count() > 0:
        return

    ava = Customer(name="Ava Banks", email="ava@example.com")
    ben = Customer(name="Ben Rivera", email="ben@example.com")
    db.add_all([ava, ben])
    db.flush()  # get IDs

    txns = [
        Transaction(customer_id=ava.id, amount=Decimal("42.50")),
        Transaction(customer_id=ava.id, amount=Decimal("19.99")),
        Transaction(customer_id=ben.id, amount=Decimal("88.00")),
    ]
    db.add_all(txns)
    db.commit()
