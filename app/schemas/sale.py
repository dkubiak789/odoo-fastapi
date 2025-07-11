from datetime import datetime
from decimal import Decimal
from typing import Any, List, Optional, Union

from pydantic import BaseModel, condecimal, field_validator


class SaleOrderLineBase(BaseModel):
    """
    Base schema for Sale Order Line items.

    Attributes:
        product_id: ID of the product being sold
        product_uom_qty: Quantity ordered
        price_unit: Unit price
        price_subtotal: Subtotal for this line
    """

    product_id: int
    product_uom_qty: condecimal(ge=Decimal("0"))
    price_unit: condecimal(ge=Decimal("0"))
    price_subtotal: condecimal(ge=Decimal("0"))

    @field_validator("product_id", mode="before")
    @classmethod
    def extract_id_from_tuple(cls, v: Any) -> int:
        """Extract ID from Odoo's (id, name) tuple format"""
        if isinstance(v, list) and len(v) == 2:
            return v[0]
        return v


class SaleOrderBase(BaseModel):
    """
    Base schema for Sale Order with common attributes.

    Attributes:
        partner_id: Customer ID
        date_order: Order date and time
        amount_total: Total amount of the order
        state: Order status
        invoice_status: Invoice status of the order
    """

    partner_id: int
    date_order: datetime
    amount_total: condecimal(ge=Decimal("0"))
    state: str
    invoice_status: str

    @field_validator("partner_id", mode="before")
    @classmethod
    def extract_id_from_tuple(cls, v: Any) -> int:
        """Extract ID from Odoo's (id, name) tuple format"""
        if isinstance(v, list) and len(v) == 2:
            return v[0]
        return v


class SaleOrder(SaleOrderBase):
    """
    Complete Sale Order schema including lines and ID.

    Attributes:
        id: The unique identifier for the sale order
        name: The order reference number
        order_lines: List of order lines
    """

    id: int
    name: str
    order_lines: List[SaleOrderLineBase]

    class Config:
        """Pydantic config for the SaleOrder model."""

        from_attributes = True
