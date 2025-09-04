import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from .database import engine, Base, SessionLocal
from .auth import mint_jwt
from .schemas import LoginIn, TokenOut
from .routers import customers, transactions

app = FastAPI(title="Syntropy Mini API")

# Allow the Vue dev server to call the API
origin = os.getenv("CORS_ORIGIN", "http://localhost:5173")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# For the demo: create tables at startup
with engine.begin() as conn:
    Base.metadata.create_all(bind=conn)

@app.get("/health")
def health():
    with SessionLocal() as s:
        s.execute(text("SELECT 1"))
    return {"ok": True}

@app.post("/auth/login", response_model=TokenOut)
def login(body: LoginIn):
    if body.username != "admin" or body.password != "admin":
        from fastapi import HTTPException; raise HTTPException(status_code=401, detail="bad creds")
    return {"access_token": mint_jwt("admin")}

# Mount routers
app.include_router(customers.router)
app.include_router(transactions.router)
