from fastapi import FastAPI
import requests

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


def retrieve_disease_omim(diseaseId):
    endpoint= f"https://hpo.jax.org/api/hpo/disease/{diseaseId}"
    headers = {'accept': 'application/json'}
    response = requests.get(url = endpoint, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return response.text 



@app.get("/")
async def root():
    return {"message": "Genomiki HPO API"}






@app.get("/phenotype/")
async def retrieve_terms_using_the_phenotype(search_term: str, max: int = -1):
    data = {
        "q": search_term,
        "category": "diseases",
        "max": max
    }
    response = retrieve_terms(data)
    disease_list = response['diseases']
    result = []
    for disease in disease_list:
        res = retrieve_disease_omim(disease['diseaseId'])
        result.append({res['disease']['diseaseName']: res})
    return result

