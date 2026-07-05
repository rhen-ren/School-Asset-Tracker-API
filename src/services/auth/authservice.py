import os
from dotenv import load_dotenv
import jwt

#get secret key from env
load_dotenv()
SECRETKEY = os.getenv("SECRETKEY")
ALGORITHM = "HS256"



#access token creation
#uses jwt
def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRETKEY, algorithm=ALGORITHM)
    return encoded_jwt


