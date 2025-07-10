"""
Products endpoints module.

This module contains all the API endpoints for product-related operations.
"""

from typing import List

from fastapi import APIRouter, HTTPException

from ....core.constants import PRODUCT_FIELDS
from ....schemas.product import Product
from ....services.odoo import odoo

router = APIRouter()


@router.get("", response_model=List[Product])
async def get_products(limit: int = 10):
    """
    Get products from Odoo.

    Retrieves a list of products from Odoo with optional limit.

    Args:
        limit: Maximum number of products to return (default: 10)

    Returns:
        List[Product]: List of products

    Raises:
        HTTPException: If there's an error fetching products from Odoo
    """
    products = await odoo.fetch_records(
        model="product.template", domain=[], fields=PRODUCT_FIELDS, limit=limit
    )
    return products


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """
    Get a single product from Odoo.

    Retrieves a specific product by its ID.

    Args:
        product_id: The unique identifier of the product

    Returns:
        Product: The requested product

    Raises:
        HTTPException: If the product is not found or there's an error fetching from Odoo
    """
    products = await odoo.fetch_records(
        model="product.template",
        domain=[["id", "=", product_id]],
        fields=PRODUCT_FIELDS,
    )

    if not products:
        raise HTTPException(status_code=404, detail="Product not found")

    return products[0]
