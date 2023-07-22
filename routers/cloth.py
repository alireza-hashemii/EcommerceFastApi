from fastapi import APIRouter, UploadFile , Depends
from sqlalchemy.orm import Session
from db.database import get_db
from service import product
import os
import time


router = APIRouter()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR,"files")


strtime = time.strftime("%H")


@router.post("/file/upload")
def upload_a_file(
    name:str,
    gender:str,
    category:str,
    price:float,
    detail:str, 
    file: UploadFile, 
    db: Session = Depends(get_db)
    ):

    new_filename = "{}_{}.png".format(os.path.splitext(file.filename)[0], strtime)
    SAVE_FILE_PATH = os.path.join(UPLOAD_DIR, new_filename)
    with open(SAVE_FILE_PATH, "wb") as f:
        f.write(file.file.read())
    

    return product.add_product(name,gender,category,detail,price,db,SAVE_FILE_PATH)



