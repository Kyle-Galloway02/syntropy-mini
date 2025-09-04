from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
import os

SECRET = os.getenv("JWT_SECRET", "devsecret")
ALG = "HS256"
bearer = HTTPBearer()

def get_current_user(token=Depends(bearer)):
    try:
        payload = jwt.decode(token.credentials, SECRET, algorithms=[ALG])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
