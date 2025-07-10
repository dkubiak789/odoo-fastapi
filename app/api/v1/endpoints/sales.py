"""
Sales endpoints module.

This module contains all the API endpoints for sale order-related operations.
"""

from typing import List

from fastapi import APIRouter, HTTPException

from ....core.constants import SALE_ORDER_FIELDS, SALE_ORDER_LINE_FIELDS
from ....schemas.sale import SaleOrder
from ....services.odoo import odoo

router = APIRouter()


@router.get("", response_model=List[SaleOrder])
async def get_sale_orders(limit: int = 10):
    """
    Get sale orders from Odoo.

    Retrieves a list of sale orders with their lines from Odoo.

    Args:
        limit: Maximum number of orders to return (default: 10)

    Returns:
        List[SaleOrder]: List of sale orders with their lines

    Raises:
        HTTPException: If there's an error fetching orders from Odoo
    """
    orders = await odoo.fetch_records(
        model="sale.order", domain=[], fields=SALE_ORDER_FIELDS, limit=limit
    )

    # Fetch order lines for each order
    for order in orders:
        order_lines = await odoo.fetch_records(
            model="sale.order.line",
            domain=[("order_id", "=", order["id"])],
            fields=SALE_ORDER_LINE_FIELDS,
        )
        order["order_lines"] = order_lines

    return orders


@router.get("/{order_id}", response_model=SaleOrder)
async def get_sale_order(order_id: int):
    """
    Get a single sale order from Odoo.

    Retrieves a specific sale order by its ID, including all order lines.

    Args:
        order_id: The unique identifier of the sale order

    Returns:
        SaleOrder: The requested sale order with its lines

    Raises:
        HTTPException: If the order is not found or there's an error fetching from Odoo
    """
    orders = await odoo.fetch_records(
        model="sale.order", domain=[["id", "=", order_id]], fields=SALE_ORDER_FIELDS
    )

    if not orders:
        raise HTTPException(status_code=404, detail="Sale order not found")

    order = orders[0]

    # Fetch order lines
    order_lines = await odoo.fetch_records(
        model="sale.order.line",
        domain=[("order_id", "=", order_id)],
        fields=SALE_ORDER_LINE_FIELDS,
    )
    order["order_lines"] = order_lines

    return order


@router.get("/{order_id}/lines", response_model=List[dict])
async def get_sale_order_lines(order_id: int):
    """
    Get lines for a specific sale order.

    Retrieves all order lines associated with a specific sale order.

    Args:
        order_id: The unique identifier of the sale order

    Returns:
        List[dict]: List of order lines for the specified order

    Raises:
        HTTPException: If the order lines cannot be fetched or the order doesn't exist
    """
    order_lines = await odoo.fetch_records(
        model="sale.order.line",
        domain=[("order_id", "=", order_id)],
        fields=SALE_ORDER_LINE_FIELDS,
    )

    if not order_lines:
        raise HTTPException(
            status_code=404, detail="No order lines found for this order"
        )

    return order_lines
