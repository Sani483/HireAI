from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models import User
from app.services.auth import SECRET_KEY, ALGORITHM


bearer_scheme = HTTPBearer()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        user_id = int(user_id)

    except (JWTError, ValueError):
        raise credentials_exception

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise credentials_exception

    return user