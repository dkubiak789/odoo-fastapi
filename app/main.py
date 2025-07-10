from fastapi import FastAPI, HTTPException
from xmlrpc import client
from .config import settings

app = FastAPI(title="Odoo FastAPI Integration")


def get_odoo_client():
    """Create and return an Odoo XML-RPC client"""
    common = client.ServerProxy(f'{settings.odoo_url}/xmlrpc/2/common')
    uid = common.authenticate(
        settings.odoo_db,
        settings.odoo_username,
        settings.odoo_password,
        {}
    )
    if not uid:
        raise HTTPException(status_code=401, detail="Odoo authentication failed")

    models = client.ServerProxy(f'{settings.odoo_url}/xmlrpc/2/object')
    return models, uid


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Odoo FastAPI Integration",
        "endpoints": {
            "partners": "/partners",
            "products": "/products"
        }
    }


@app.get("/partners")
async def get_partners(limit: int = 10):
    """Get partners from Odoo"""
    try:
        models, uid = get_odoo_client()
        partners = models.execute_kw(
            settings.odoo_db,
            uid,
            settings.odoo_password,
            'res.partner',
            'search_read',
            [[['is_company', '=', True]]],
            {'fields': ['name', 'email', 'phone'], 'limit': limit}
        )
        return {"partners": partners}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/products")
async def get_products(limit: int = 10):
    """Get products from Odoo"""
    try:
        models, uid = get_odoo_client()
        products = models.execute_kw(
            settings.odoo_db,
            uid,
            settings.odoo_password,
            'product.template',
            'search_read',
            [[]],
            {'fields': ['name', 'list_price', 'default_code'], 'limit': limit}
        )
        return {"products": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))