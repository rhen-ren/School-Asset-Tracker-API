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
    
#handle update of categories
#only the user that created the category can update
def update_category(category_id: int, user_id: int, categroy_name: str, category_description: str, db: Session) -> Category:
    try:
        current_category: Category = db.get(Category, category_id)

        if not current_category:
            raise HTTPException(status_code=404)
        
        if current_category.user_id == user_id:
            current_category.name = categroy_name
            current_category.description = category_description
            db.commit()
            db.refresh(current_category)
            return current_category
        else:
            raise HTTPException(status_code=401)
    except:
        raise HTTPException(status_code=400)


