# Odoo FastAPI Integration

A FastAPI application that provides a REST API interface for Odoo 18. This project allows you to interact with Odoo through modern REST API endpoints instead of direct XML-RPC calls.

## License

Copyright (C) 2025 Dariusz Kubiak <dkubiak.pl@gmail.com>

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0) or later.
See [https://www.gnu.org/licenses/agpl](https://www.gnu.org/licenses/agpl) for full license text.

## Features

- REST API interface for Odoo
- Swagger UI documentation
- Partners, Products and Sales Orders endpoints
- Easy configuration through environment variables
- Asynchronous request handling

## Prerequisites

- Python 3.11.8 or higher
- Poetry package manager
- Running Odoo 18 instance
- Access to Odoo database

## Installation

1. Clone the repository and set up the environment:
```bash
git clone git@github.com:dkubiak789/odoo-fastapi.git
cd odoo-fastapi
pyenv virtualenv 3.11.8 odoo-fastapi
pyenv local odoo-fastapi
pip install poetry
poetry install --no-root
```

2. Configure environment variables:
```bash
cp .env.example .env
```

3. Start the development server:
```bash
poetry run uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`

## API Endpoints

### Root
- `GET /` - Welcome message and available endpoints

### Partners
- `GET /partners` - Get list of partners
  - Query Parameters:
    - `limit` (optional): Number of records to return (default: 10)

### Products
- `GET /products` - Get list of products
  - Query Parameters:
    - `limit` (optional): Number of records to return (default: 10)

### Sales Orders
- `GET /orders` - Get list of sales orders
  - Query Parameters:
    - `limit` (optional): Number of records to return (default: 10)

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Contact

Dariusz Kubiak - dkubiak.pl@gmail.com

Project Link: [https://github.com/dkubiak789/odoo-fastapi](https://github.com/dkubiak789/odoo-fastapi)
```
