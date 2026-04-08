from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()





@app.get("/")
def home():
    return {"message": "it works!"} 

@app.get("/joke")    
def get_joke():
    with open("jokes.txt") as f:
        jokes = f.readlines()
    return {"joke": random.choice(jokes).strip()}



