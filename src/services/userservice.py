from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.auth.token import Token
from src.services.auth import authservice
from fastapi.exceptions import HTTPException

#handle user login
def login_user(email: str, password: str, db: Session) -> Token:
    try:
        #check if login info in database
        user: User = authservice.authenticate_user(email, password, db)
        #generate token for user
        if user:
            token: Token = authservice.create_access_token(data = {"email": user.email})
            return token
    except Exception as e:
        raise e
    
#handle user account creation
def signup_user(name: str, email: str, password: str, role: str, db: Session):
    try:
        #add user to the database
        if name and email and password and role:
            new_user = User(
                name = name,
                email = email,
                password = authservice.hash_password(password),
                role = role
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            if new_user:
                token: Token = authservice.create_access_token(data = {"email": new_user.email})
                return token
        else:
            raise HTTPException(status_code=400)
    except Exception as e:
        raise e

        