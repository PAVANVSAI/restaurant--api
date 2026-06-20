from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

SECRET = "your_secret_key_123"
bearer = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")