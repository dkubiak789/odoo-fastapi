"""
FastAPI main application module.

This module initializes the FastAPI application and sets up the core configuration,
including API routers, documentation, and the root endpoint.

The application serves as a REST API interface for Odoo, providing modern HTTP endpoints
instead of direct XML-RPC calls.

Attributes:
    app: The main FastAPI application instance
    api_router: Router containing all API version 1 endpoints
    settings: Application configuration settings
"""

from fastapi import FastAPI

from .api.v1.router import api_router
from .core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="REST API interface for Odoo",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Include API router with version prefix
app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/")
async def root():
    """
    Root endpoint providing API information and documentation links.

    This endpoint serves as the entry point to the API, providing basic information
    about the service and links to the available documentation.

    Returns:
        dict: A dictionary containing:
            - message: Welcome message with the application name
            - version: Current API version
            - documentation: Dictionary with links to Swagger and ReDoc documentation
            - api_version: Current API version string
            - api_prefix: API version prefix for all endpoints

    Example:
        {
            "message": "Welcome to Odoo FastAPI Integration",
            "version": "1.0.0",
            "documentation": {
                "swagger": "/docs",
                "redoc": "/redoc"
            },
            "api_version": "v1",
            "api_prefix": "/api/v1"
        }
    """
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": "1.0.0",
        "documentation": {"swagger": "/docs", "redoc": "/redoc"},
        "api_version": "v1",
        "api_prefix": settings.api_v1_prefix,
    }
