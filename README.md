# Odoo FastAPI Integration

A FastAPI application that provides a REST API interface for Odoo 18. This project allows you to interact with Odoo through modern REST API endpoints instead of direct XML-RPC calls.

## Features

- REST API interface for Odoo
- Swagger UI documentation
- Partners and Products endpoints
- Easy configuration through environment variables
- Asynchronous request handling

## Prerequisites

- Python 3.11.7 or higher
- Poetry package manager
- Running Odoo 18 instance
- Access to Odoo database

## Installation

1. Clone the repository:
```bash
git clone git@github.com:dkubiak789/odoo-fastapi.git cd odoo-fastapi
``` 

2. Install dependencies using Poetry:
```bash
poetry install
``` 

3. Create a `.env` file in the root directory:
```bash
cp .env.example .env
``` 

4. Configure your Odoo connection details in `.env`:
```ini 
ODOO_URL=[http://localhost:8069](http://localhost:8069) ODOO_DB=your_database ODOO_USERNAME=your_username ODOO_PASSWORD=your_password
``` 

## Running the Application

1. Activate the poetry shell:
```bash
poetry shell
``` 

2. Run the FastAPI application:
```bash
uvicorn app.main:app --reload
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

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure
```
odoo-fastapi/ 
├── app/ 
├── __init__.py 
│ ├── main.py 
│ └── config.py 
├── .env 
├── .env.example 
├── pyproject.toml 
└── README.md
``` 

## Development

To add new endpoints or modify existing ones, edit the `app/main.py` file. The project uses:

- FastAPI for the web framework
- Pydantic for data validation
- Python's built-in xmlrpc.client for Odoo communication
- python-dotenv for environment variable management

## Error Handling

The API includes error handling for:
- Odoo connection issues
- Authentication failures
- Invalid requests
- Server errors

## Security Considerations

1. Never commit the `.env` file to version control
2. Use strong passwords for Odoo authentication
3. Consider implementing API authentication for production use
4. Implement rate limiting for production deployment

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Contact

Dariusz Kubiak - dkubiak.pl@gmail.com

Project Link: [https://github.com/dkubiak789/odoo-fastapi](https://github.com/dkubiak789/odoo-fastapi)
```
