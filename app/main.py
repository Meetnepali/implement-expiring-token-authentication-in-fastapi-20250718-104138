from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Customer Management API", version="1.0.0")

# Simulated in-memory customer database
db_customers = [
    {"id": 1, "name": "Alice Buyer", "active": True},
    {"id": 2, "name": "Bob Seller", "active": False},
    {"id": 3, "name": "Carla Client", "active": True}
]

class Customer(BaseModel):
    id: int
    name: str
    active: bool

class CustomerSearchResponse(BaseModel):
    customers: List[Customer]
    count: int

@app.get("/customers/search", response_model=CustomerSearchResponse, tags=["Customers"])
def search_customers(
    name: Optional[str] = Query(None, description="Customer name contains this value", min_length=1, max_length=32),
    active: Optional[bool] = Query(None, description="Filter by active status (true/false)")
):
    try:
        results = db_customers
        if name is not None:
            results = [c for c in results if name.lower() in c["name"].lower()]
        if active is not None:
            results = [c for c in results if c["active"] == active]
        # Convert to Customer objects for response model
        return CustomerSearchResponse(customers=[Customer(**c) for c in results], count=len(results))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing search: {str(e)}"
        )

@app.get("/customers/{customer_id}", response_model=Customer, tags=["Customers"])
def get_customer(customer_id: int):
    for c in db_customers:
        if c["id"] == customer_id:
            return Customer(**c)
    raise HTTPException(status_code=404, detail="Customer not found.")
