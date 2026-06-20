from fastapi import FastAPI
from database import Base, engine
import models
from routes import restaurants, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(restaurants.router)
app.include_router(auth.router)