from fastapi import FastAPI , Request , Depends
from db.database import engine
from db import models
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates
from routers import user , cloth


app = FastAPI()
app.include_router(user.router)
app.include_router(cloth.router)


templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)


# if __name__ == "__main__":
#     uvicorn.run(app=app, host="127.0.0.1",port=8500,reload_delay= True,workers= True)