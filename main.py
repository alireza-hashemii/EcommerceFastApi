from fastapi import FastAPI , Request , Depends
from db.database import engine
from db import models
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates
from routers import user


app = FastAPI()
app.include_router(user.router)

templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)

