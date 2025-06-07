from fastapi import FastAPI
from typing import Optional

app=FastAPI()

products=[
    {"id":1, "name":"redmi", "category":"mobile"},
    {"id":2, "name":"samsung", "category":"mobile"},
    {"id":3, "name":"dell", "category":"laptop"},
    {"id":4, "name":"hp", "category":"laptop"}
]

@app.get("/products/{pro_id}")
def get_product(pro_id: int):
    for pro in products:
        if pro["id"] == pro_id:
            return {"product": pro}

@app.get("/products")
def get_product(name: Optional[str] = None,limit: int = 10):
    result = products
    if name:
        result =[pro for pro in products if name.lower() in pro["name"].lower()]
    return result[:limit]