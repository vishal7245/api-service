from fastapi import FastAPI
import requests
from enum import Enum

app = FastAPI()

def retrieve_terms(data):
    endpoint= "https://hpo.jax.org/api/hpo/search"
    headers = {'accept': 'application/json'}
    response = requests.get(url = endpoint, params=data, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return response.text 


@app.get("/")
async def root():
    return {"message": "Genomiki HPO API"}




class Category(str, Enum):
    TERMS = "terms"
    GENES = "genes"
    DISEASES = "diseases"

@app.post("/phenotype/{Category}")
async def retrieve_terms_using_the_phenotype(cat: Category, search_term: str, max: int = -1):
    data = {
        "q": search_term,
        "category": cat,
        "max": max
    }
    response = retrieve_terms(data)
    return response

