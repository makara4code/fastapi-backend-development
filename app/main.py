from fastapi import FastAPI
from app.routers import products

# class instantiation
# instance =  Class()
app = FastAPI()


# get, post, put, patch, delete ...
@app.get("/")
def home():
    return {"message": "Hello to FastAPI"}


app.include_router(products.api_router)
