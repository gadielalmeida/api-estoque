from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Estoque")

products = []
id_counter = 1

class Product(BaseModel):
    name: str
    quantity: int

@app.get("/")
def home():
    return {"status": "API de estoque rodando"}

@app.post("/products")
def create_product(product: Product):
    global id_counter

    new_product = {
        "id": id_counter,
        "name": product.name,
        "quantity": product.quantity
    }

    id_counter += 1
    products.append(new_product)

    return new_product

@app.get("/products")
def list_products():
    return products
    
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Produto não encontrado"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_product.name
            product["quantity"] = updated_product.quantity
            return product
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Produto removido com sucesso"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")