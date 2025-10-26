from pydantic import BaseModel
from typing import Annotated
from fastapi import APIRouter, Query


class Pagination(BaseModel):
    page: int
    item: int


class Product(BaseModel):
    id: int
    name: str


api_router = APIRouter()


@api_router.get("/products")
def get_products(pagination: Annotated[Pagination, Query()]):
    products = [{"id": 1, "name": "Shoes"}]
    return {
        "products": products,
        "page": pagination.page,
        "item": pagination.item,
    }


@api_router.post("/products")
def create_new_product(product: Product):
    return {"product": product}
