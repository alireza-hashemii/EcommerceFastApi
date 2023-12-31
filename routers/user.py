from fastapi import APIRouter, Depends, Form, status
from fastapi import Request
from sqlalchemy.orm import Session
from db.database import get_db
from starlette.responses import RedirectResponse
from db import models
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session



router = APIRouter()

templates = Jinja2Templates(directory="templates")



@router.get("/")
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@router.get("/home")
def home(request: Request,db:Session = Depends(get_db)):
    products = db.query(models.Cloth).all()
    return templates.TemplateResponse("home.html", {"request": request,"products":products})


@router.post("/add")
def user_add(request: Request,
             username: str = Form(
                 media_type="application/x-www-form-urlencoded"),
             email: str = Form(media_type="application/x-www-form-urlencoded"),
             password: int = Form(
                 media_type="application/x-www-form-urlencoded"),
             db: Session = Depends(get_db)
             ):

    url = router.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@router.get("/update")
def user_update():
    pass


@router.get("/read")
def user_read():
    pass


@router.get("/delete")
def user_delete():
    pass
