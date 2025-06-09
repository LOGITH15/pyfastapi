from fastapi import Depends, FastAPI,Request
from fastapi.responses import JSONResponse
import time
from fastapi import Header

app=FastAPI()
datas=[
    {"id":1, "name":"log", "age":20},
    {"id":2, "name":"kkp", "age":15},
    {"id":3, "name":"abi", "age":32}
]

def check_key(my_secret_key: str = Header(..., description="Secret key to access the endpoint")):
    if my_secret_key != "secretkfjf":
        return JSONResponse(status_code=401, content={"message": "unauthorized request"})
    return my_secret_key

@app.middleware("http")
async def verify_user(request: Request, call_next):
   
   
   
   start_time = time.time()
   if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
        return await call_next(request)
   response = await call_next(request)
   process_time = time.time() - start_time
   print(f"Request processed in {process_time:.4f}'s")
   return response


@app.get("/user/{id}")
def get_user(id: int,_: str = Depends(check_key)):
    for user in datas:
        if user["id"] == id:
            return user
    return  JSONResponse(
        status_code=404,
        detail=f"User with id {id} not found."
    )