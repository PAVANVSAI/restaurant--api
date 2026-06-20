from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserSignup, UserLogin
from passlib.context import CryptContext
from jose import jwt

router = APIRouter()

# for hashing passwords
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
# secret key - in real apps this is hidden in environment variables
SECRET = "your_secret_key_123"

# SIGNUP
@router.post("/signup")
def signup(data: UserSignup, db: Session = Depends(get_db)):
    # check if email already exists
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # hash the password - never store plain text
    hashed = pwd.hash(data.password)

    # save user
    new_user = User(email=data.email, password=hashed)
    db.add(new_user)
    db.commit()
    return {"message": "Account created!"}

# LOGIN
@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    # find user by email
    user = db.query(User).filter(User.email == data.email).first()

    # check if user exists and password matches
    if not user or not pwd.verify(data.password, user.password):
        raise HTTPException(status_code=401, detail="Wrong email or password")

    # create JWT token
    token = jwt.encode({"user_id": user.id}, SECRET, algorithm="HS256")
    return {"token": token}