from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "you're a coder!"}

@app.get("/hello")
def send_message():
    return {"Message": "what up"}