from fastapi import FastAPI

import requests 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

url= "https://rickandmortyapi.com/api/character"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/character/{id}")
def get_character(id:int):
    result = requests.get(f"{url}/{id}")
    print (result) 
    return result.json()
