from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Project endpoints
# ...
# Blog post endpoints
# ...
# Contact endpoints
# ...

