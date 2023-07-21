from fastapi import APIRouter, UploadFile , Depends
from pydmodels.models import PCloth
from db.models import Cloth
from sqlalchemy.orm import Session
from db.database import get_db
import os
import time
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR,"files")


router = APIRouter()
@router.post("/file/upload")
def upload_a_file(cloth: PCloth, file: UploadFile, db: Session = Depends(get_db)):

    new_filename = "{}.png".format(str(cloth.name))
    SAVE_FILE_PATH = os.path.join(UPLOAD_DIR,new_filename)
    with open(SAVE_FILE_PATH,"wb") as f:
        f.write(file.file.read())
    

    new_cloth = Cloth(
        price = cloth.price,
        name = cloth.name,
        category = cloth.category,
        gender = cloth.gender,
        detail = cloth.detail,
        image = SAVE_FILE_PATH
    )
    
    db.add(new_cloth)
    db.commit()
    db.refresh(new_cloth)
 
    return new_cloth


# @router.post("/add/cloth")
# def add_cloth(cloth: PCloth, file: UploadFile ,db: Session = Depends(get_db)):
#     pass




    # new_cloth = Cloth(
    #     price = cloth.price,
    #     name = cloth.name,
    #     category = cloth.category,
    #     gender = cloth.gender,
    #     detail = cloth.detail,
    #     image = out_file
    # )
    
    # db.add(new_cloth)
    # db.refresh(new_cloth)
    # db.commit()
    