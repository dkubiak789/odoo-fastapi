#!/bin/bash
# Starts the FastAPI development server using Uvicorn with hot reload enabled.
poetry run uvicorn app.main:app --reload
