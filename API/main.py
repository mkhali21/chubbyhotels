from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

# Sample in-memory database with properties
properties = [
    {
        "id": str(uuid.uuid4()),  # Generate unique ID
        "Name": "Luxury Villa",
        "Country": "USA",
        "City": "Los Angeles",
        "Image": "images/villa.jpg",
        "ischubby": False,
        "isactive": True
    },
    {
        "id": str(uuid.uuid4()),
        "Name": "Cozy Cottage",
        "Country": "UK",
        "City": "London",
        "Image": "images/cottage.jpg",
        "ischubby": True,
        "isactive": True
    },
    {
        "id": str(uuid.uuid4()),
        "Name": "Modern Apartment",
        "Country": "Canada",
        "City": "Toronto",
        "Image": "images/apartment.jpg",
        "ischubby": False,
        "isactive": False
    }
]

# Pydantic model for request validation
class Property(BaseModel):
    Name: str
    Country: str
    City: str
    Image: str  # URL or file path
    ischubby: bool
    isactive: bool

class PropertyResponse(Property):
    id: str  # Unique property ID

@app.get("/properties", response_model=List[PropertyResponse])
def get_all_properties():
    """Fetch all properties."""
    return properties

@app.get("/properties/{property_id}", response_model=PropertyResponse)
def get_property_by_id(property_id: str):
    """Fetch a specific property by its ID."""
    for property in properties:
        if property["id"] == property_id:
            return property
    raise HTTPException(status_code=404, detail="Property not found")

@app.post("/properties", response_model=PropertyResponse)
def add_property(property: Property):
    """Add a new property listing."""
    new_property = property.dict()
    new_property["id"] = str(uuid.uuid4())  # Generate unique ID
    properties.append(new_property)
    return new_property
