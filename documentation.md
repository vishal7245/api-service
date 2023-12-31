# Genomiki HPO API Documentation

## Introduction

The Genomiki HPO API provides a simple interface for retrieving information related to Human Phenotype Ontology (HPO). This API is built using the FastAPI framework and facilitates the retrieval of terms and associated diseases from the HPO database.

## API Endpoints

### 1. Root Endpoint

- **URL:** `/`
- **HTTP Method:** `GET`
- **Description:** Returns a welcome message indicating the presence of the Genomiki HPO API.

#### Example

```json
{
    "message": "Genomiki HPO API"
}
```

### 2. Retrieve Terms Using the Phenotype Endpoint

- **URL:** `/phenotype/`
- **HTTP Method:** `GET`
- **Parameters:**
  - `search_term` (required): The search term for retrieving HPO terms.
  - `max` (optional): The maximum number of results to return. Default is set to -1, which returns all available results.

#### Example

- **Request:**

```http
GET /phenotype/?search_term=cancer&max=5
```

- **Response:**

```json
[
    {
        "Cancer": {
            "disease": {
                "diseaseId": "OMIM:114480",
                "diseaseName": "Breast cancer"
                // Additional disease information
            }
        }
    },
    // Additional results
]
```

## Functions

### 1. `retrieve_terms(data: dict) -> dict`

- **Description:** Retrieves HPO terms based on the provided search criteria.
- **Parameters:**
  - `data` (dict): Dictionary containing query parameters such as `q` for the search term, `category` for the type of data to retrieve, and `max` for the maximum number of results.
- **Returns:**
  - Dictionary containing the retrieved terms and associated information.

### 2. `retrieve_disease_omim(diseaseId: str) -> dict`

- **Description:** Retrieves detailed information about a specific disease based on its OMIM identifier.
- **Parameters:**
  - `diseaseId` (str): The OMIM identifier of the disease.
- **Returns:**
  - Dictionary containing detailed information about the specified disease.

## Usage

1. Access the root endpoint to confirm the presence of the Genomiki HPO API.
2. Use the `/phenotype/` endpoint to retrieve HPO terms based on a specified search term.

### Note

- The API interacts with the HPO database using the JAX REST API.
- Error responses, if any, will include relevant error messages.
- Ensure proper authentication and authorization mechanisms are in place, especially if deploying in a production environment.
