#!/bin/bash
# FastAPI Development Server Startup Script
#
# This script starts the FastAPI development server using Uvicorn with hot reload enabled.
#
# Features:
# - Hot reload: Automatically restarts the server when code changes are detected
# - Debug mode: Provides detailed error information
# - Watch mode: Monitors project files for changes
# - Host: Binds to localhost (127.0.0.1)
# - Port: Uses port 8000 by default
#
# Usage:
#    ./start.sh          # Start server with default settings
#    ./start.sh --help   # Show available options
#
# Environment:
#    - Uses Poetry for dependency management
#    - Requires Python 3.11.7 or higher
#    - Loads environment variables from .env file
#
# Documentation:
#    - API documentation available at http://127.0.0.1:8000/docs
#    - ReDoc alternative at http://127.0.0.1:8000/redoc

poetry run uvicorn app.main:app --reload
