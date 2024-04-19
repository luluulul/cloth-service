from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException


app = FastAPI(openapi_url="/api/v1/cloths/openapi.json", docs_url="/api/v1/cloths/docs")

cloths_router = APIRouter()

cloths = [
    {'cloths_id': 1,
     'name': 'Kany West',
     'brand': '47',
     'genre': '1 billion',
     'price': 'rap, R&B, electronic, gospel'},
    {'cloths_id': 2,
     'name': 'Валерий Меладзе',
     'brand': '58',
     'genre': '45 millions',
     'price': 'поп, рок, эстрадная песня'},
    {'cloths_id': 3,
     'name': 'Billie Eilish',
     'brand': '22',
     'genre': '300 millions',
     'price': 'rap, pop'},
    {'cloths_id': 4,
     'name': 'The Weeknd',
     'brand': '34',
     'genre': '700 millions',
     'price': 'rap, R&B'},
    {'cloths_id': 5,
     'name': 'Eminem',
     'brand': '51',
     'genre': '1 billion',
     'price': 'rap, hip-hop'}
]


@cloths_router.get("/")
async def read_cloths():
    return cloths


@cloths_router.get("/{cloths_id}")
async def read_artist(cloths_id: int):
    for cloth in cloths:
        if cloth['cloths_id'] == cloths_id:
            return cloth
    return None

app.include_router(cloths_router, prefix='/api/v1/cloths', tags=['cloths'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)