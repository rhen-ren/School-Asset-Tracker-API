from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.category import Category
from fastapi.exceptions import HTTPException

#handle getting of categories
def get_categories(db: Session):
    categories:list[Category] = db.execute(select(Category)).scalars().all()
    return categories

#handle creation of categories
def create_category(user_id: int, category_name: str, categeory_description: str, db: Session) -> Category:
    try:
        new_category = Category(
            name = category_name,
            description = categeory_description,
            user_id = user_id
        )
        db.add(new_category)
        db.commit()
        db.refresh(new_category)

        return new_category
    except:
        raise HTTPException(status_code=400)

