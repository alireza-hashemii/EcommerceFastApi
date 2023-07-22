from db.models import Cloth as ClothModel
from sqlalchemy.orm import Session


def add_product(
        name:str,
        gender:str,
        category:str,
        detail:str,
        price:float,
        db: Session,
        filepath: str
    ):
    new_cloth = ClothModel(
        name = name,
        gender = gender,
        category = category,
        detail = detail,
        price = price,
        image = filepath
    )

    db.add(new_cloth)
    db.commit()
    db.refresh(new_cloth)
    return new_cloth