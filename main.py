from fastapi import FastAPI, HTTPException
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
    return {"message": "Backend is running"}


@app.get("/character/{id}")
def get_character(id:int):
    try:
        result = requests.get(f"{url}/{id}")
        if result.status_code == 404:
            raise HTTPException(status_code=404, detail="Character not found")
        return result.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

#endpoint
@app.get("/characters")
def get_multiple_characters(limit: int = 5):
    result = requests.get(url)
    data = result.json()
    return data["results"][:limit]
def get_character(id:int):
    result = requests.get(f"{url}/{id}")
    print (result) 
    return result.json()

