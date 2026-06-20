from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import Base, engine
import models
from routes import restaurants, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(restaurants.router)
app.include_router(auth.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")