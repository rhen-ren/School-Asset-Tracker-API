import os
from dotenv import load_dotenv

load_dotenv()
SECRETKEY = os.getenv("SECRETKEY")
ALGORITHM = "HS256"