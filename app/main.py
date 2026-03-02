from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="API de Estoque")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo
class Product(BaseModel):
    name: str
    quantity: int
    price: float

# Banco fake em memória
products = []

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/products")
def list_products():
    return products

@app.post("/products")
def create_product(product: Product):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "quantity": product.quantity,
        "price": product.price
    }
    products.append(new_product)
    return new_product