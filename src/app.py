from typing import Union
from fastapi import FastAPI
from models import Message
import uvicorn



app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/greet")
def greet_user(message: Message):
    return {"message": f"Hello {message.name}"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080)