"""Constants used throughout the application"""

# Field definitions for Odoo models
PARTNER_FIELDS = ["name", "email", "phone"]

PRODUCT_FIELDS = ["name", "list_price", "default_code"]

SALE_ORDER_FIELDS = [
    "name",  # Order reference
    "date_order",  # Order date
    "partner_id",  # Customer
    "amount_total",  # Total amount
    "state",  # Status
    "invoice_status",  # Invoice status
]

SALE_ORDER_LINE_FIELDS = [
    "product_id",  # Product
    "product_uom_qty",  # Quantity
    "price_unit",  # Unit price
    "price_subtotal",  # Subtotal
]
