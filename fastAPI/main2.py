from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "This works, You are working with FastAPI!"}

@app.get("/hello")
def send_message():
    return {"message": "What's up?"}