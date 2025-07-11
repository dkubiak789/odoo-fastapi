"""Constants used throughout the application"""

# Field definitions for Odoo models
PARTNER_FIELDS = ["name", "email", "phone"]

PRODUCT_FIELDS = ["name", "list_price", "default_code"]

SALE_ORDER_FIELDS = [
    "name",
    "date_order",
    "partner_id",
    "amount_total",
    "state",
]

SALE_ORDER_LINE_FIELDS = [
    "product_id",
    "product_uom_qty",
    "price_unit",
    "price_subtotal",
]
