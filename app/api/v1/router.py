from fastapi import APIRouter

from .endpoints import partners, products, sales

api_router = APIRouter()

api_router.include_router(partners.router, prefix="/partners", tags=["partners"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(sales.router, prefix="/sales", tags=["sales"])
