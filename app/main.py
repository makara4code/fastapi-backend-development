from fastapi import FastAPI

# class instantiation
# instance =  Class()
app = FastAPI()


# get, post, put, patch, delete ...
@app.get("/")
def home():
    return {"message": "Hello to FastAPI"}
