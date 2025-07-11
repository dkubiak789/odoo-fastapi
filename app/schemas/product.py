from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, condecimal, constr, field_validator


class ProductBase(BaseModel):
    """
    Base schema for Product with common attributes.

    Attributes:
        name: The product name
        list_price: The product's list price
        default_code: Optional internal reference (SKU)
    """

    name: constr(min_length=1, max_length=255)
    list_price: condecimal(ge=Decimal("0"))
    default_code: Optional[str] = None

    @field_validator("default_code", mode="before")
    @classmethod
    def convert_false_to_none(cls, v):
        if v is False:
            return None
        return v


class ProductCreate(ProductBase):
    """Schema for creating a new product."""

    pass


class ProductUpdate(ProductBase):
    """Schema for updating an existing product."""

    name: Optional[constr(min_length=1, max_length=255)] = None
    list_price: Optional[condecimal(ge=Decimal("0"))] = None


class Product(ProductBase):
    """
    Schema for product response including database id.

    Attributes:
        id: The unique identifier for the product
    """

    id: int

    class Config:
        """Pydantic config for the Product model."""

        from_attributes = True
