from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from main import User

app=FastAPI()

datas=[
    {"id":1, "name":"John", "age":30},
    {"id":2, "name":"Jane", "age":25},
    {"id":3, "name":"Doe", "age":22}]

class ItemNotFound(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

@app.exception_handler(ItemNotFound)
async def item_not_found_handler(request: Request, excp: ItemNotFound):
    return JSONResponse(
        status_code=404,
        content={"message": f"Item with id {excp.user_id} not found."}
    )
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, excp: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"message": "Validation error",
                  "errors": excp.errors(),
                    "body": excp.body
                      if excp.body is not None
                        else "No body provided",
                  "request": request.url.path}
    )

@app.get("/users/{id}")
async def get_user(id:int):
   for user in datas:
       if user["id"] == id:
           return user
   raise ItemNotFound(id)