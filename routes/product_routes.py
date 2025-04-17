from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_products():
    return {"products": ["Laptop", "Phone", "Tablet"]}
