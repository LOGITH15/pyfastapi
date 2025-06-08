from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from fastapi import status

app=FastAPI()

user_db=[]

class UserInput(BaseModel):
    username: str =Field(...,example="min5letters", min_length=5, max_length=20)
    email: EmailStr =Field(..., example="user@gamil.com")
    password: str
    salary: Optional[float]=None
    role: str

class UserOutput(BaseModel):
    id: int
    username: str
    email: EmailStr
    salary: Optional[float]=None
    role: str

@app.post( "/create_user", response_model=UserOutput,status_code=status.HTTP_201_CREATED)
def create_user(user: UserInput):
    user_id = len(user_db) + 1
    user_data = user.model_dump()
    user_data["id"] = user_id
    user_db.append(user_data)
    return user_data

@app.get("/users",response_model=List[UserOutput],status_code=status.HTTP_200_OK)
def get_users():
    return user_db

@app.get("/users/{id}", response_model=UserOutput, status_code=status.HTTP_200_OK)
def get_user(id: int):
    for user in user_db:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")