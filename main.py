from fastapi import FastAPI
from routes import user_routes, product_routes

app = FastAPI()

# Include Routers
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])

@app.get("/")
def home():
    return {"message": "API is running successfully!"}
