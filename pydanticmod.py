from enum import Enum
from fastapi import Body, FastAPI, Path
from fastapi.params import Query
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

app= FastAPI()

class Profession(str, Enum):
    ENGINEER = "Engineer"
    DOCTOR = "Doctor"
    DEVELOPER= "Developer"

class WorkingArea(BaseModel):
    city: Optional[str]=None
    country: str

class NativeArea(BaseModel):
    street: str
    city: str
    pincode: int =Field(None, gt=100000, lt=999999)

class Details(BaseModel):
    name: str =Field(..., min_length=5, max_length=20)
    email:EmailStr
    age: int
    profession: Profession
    salary: float = Field(gt=10)
    address: NativeArea
    degrees: Optional[List[str]] = None
    living_area: WorkingArea 
    is_online: bool = True
    batch: int=2024

@app.post("/details/{id}")
def createdetails(id: int = Path(..., description="ID of the user",gt=100 ),
                  q: Optional[str] = Query(None,description="for search"), 
                  details: Details = Body(...)):
    return {
        "id": id,
        "query": q,
        "details": details
    }