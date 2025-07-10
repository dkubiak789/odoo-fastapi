"""
Schema exports for the application.

This module exports all schemas to make them easily importable
from other parts of the application.
"""

from .partner import Partner, PartnerCreate, PartnerUpdate
from .product import Product, ProductCreate, ProductUpdate
from .sale import SaleOrder, SaleOrderBase, SaleOrderLineBase

__all__ = [
    "Partner",
    "PartnerCreate",
    "PartnerUpdate",
    "Product",
    "ProductCreate",
    "ProductUpdate",
    "SaleOrder",
    "SaleOrderBase",
    "SaleOrderLineBase",
]
