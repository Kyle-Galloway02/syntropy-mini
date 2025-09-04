import os, time
from jose import jwt

SECRET = os.getenv("JWT_SECRET", "devsecret")
ALG = "HS256"

def mint_jwt(user_id: str) -> str:
    now = int(time.time())
    payload = {"sub": user_id, "iat": now, "exp": now + 3600}
    return jwt.encode(payload, SECRET, algorithm=ALG)
