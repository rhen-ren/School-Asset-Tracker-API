from fastapi import FastAPI
from src.db import Base, engine
import src.models
import uvicorn
from src.routers import userrouter

app = FastAPI()
app.include_router(userrouter.router)
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
