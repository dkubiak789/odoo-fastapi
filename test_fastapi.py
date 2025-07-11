"""
Odoo API Client Module

This is a simple test client for interacting with the Odoo REST API interface.
It handles authentication and provides methods to fetch data from various endpoints.

Example:
    client = OdooAPIClient(
        base_url="http://localhost:8000",
        username="admin",
        password="admin"
    )
    client.authenticate()
    partners = client.get_partners(limit=5)
"""

import argparse
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

import requests


@dataclass
class OdooAPIClient:
    """
    A client for interacting with the Odoo REST API.

    Attributes:
        base_url: The base URL of the Odoo API
        username: The username for authentication
        password: The password for authentication
        token: The JWT token received after authentication
    """

    base_url: str
    username: str
    password: str
    token: Optional[str] = None

    def authenticate(self) -> None:
        """
        Authenticate with the API and obtain an access token.

        This method sends a POST request to the token endpoint with the
        provided credentials and stores the received token for future requests.

        Raises:
            Exception: If authentication fails or the server returns an error
        """
        response = requests.post(
            f"{self.base_url}/api/v1/token",
            data={"username": self.username, "password": self.password},
        )
        if response.status_code == 200:
            self.token = response.json()["access_token"]
        else:
            raise Exception(f"Authentication failed: {response.text}")

    @property
    def headers(self) -> Dict[str, str]:
        """
        Get the headers required for authenticated requests.

        Returns:
            Dict[str, str]: Headers including the authentication token

        Raises:
            Exception: If called before authentication
        """
        if not self.token:
            raise Exception("Not authenticated. Call authenticate() first")
        return {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}

    def get_partners(self, limit: int = 10) -> List[Dict]:
        """
        Fetch partners from the API.

        Args:
            limit: Maximum number of partners to retrieve (default: 10)

        Returns:
            List[Dict]: List of partner records

        Raises:
            Exception: If the request fails or returns an error
        """
        response = requests.get(
            f"{self.base_url}/api/v1/partners",
            headers=self.headers,
            params={"limit": limit},
        )
        if response.status_code == 200:
            return response.json()
        raise Exception(f"Failed to fetch partners: {response.text}")

    def get_products(self, limit: int = 10) -> List[Dict]:
        """
        Fetch products from the API.

        Args:
            limit: Maximum number of products to retrieve (default: 10)

        Returns:
            List[Dict]: List of product records

        Raises:
            Exception: If the request fails or returns an error
        """
        response = requests.get(
            f"{self.base_url}/api/v1/products",
            headers=self.headers,
            params={"limit": limit},
        )
        if response.status_code == 200:
            return response.json()
        raise Exception(f"Failed to fetch products: {response.text}")

    def get_sales(self, limit: int = 10) -> List[Dict]:
        """
        Fetch sales orders from the API.

        Args:
            limit: Maximum number of sales orders to retrieve (default: 10)

        Returns:
            List[Dict]: List of sales order records

        Raises:
            Exception: If the request fails or returns an error
        """
        response = requests.get(
            f"{self.base_url}/api/v1/sales",
            headers=self.headers,
            params={"limit": limit},
        )
        if response.status_code == 200:
            return response.json()
        raise Exception(f"Failed to fetch sales orders: {response.text}")


def main():
    """
    Main function to demonstrate the usage of the OdooAPIClient.

    This function creates an instance of the client, authenticates,
    and fetches data from all available endpoints.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Odoo FastAPI client")
    parser.add_argument(
        "--user", "-u", required=True, help="Username for authentication"
    )
    parser.add_argument(
        "--password", "-p", required=True, help="Password for authentication"
    )
    args = parser.parse_args()

    # Initialize client
    client = OdooAPIClient(
        base_url="http://127.0.0.1:8000", username=args.user, password=args.password
    )

    try:
        # Authenticate
        client.authenticate()
        print("Successfully authenticated!")

        # Fetch partners
        partners = client.get_partners(limit=5)
        print("\nPartners:")
        print(json.dumps(partners, indent=2))

        # Fetch products
        products = client.get_products(limit=5)
        print("\nProducts:")
        print(json.dumps(products, indent=2))

        # Fetch sales orders
        sales = client.get_sales(limit=5)
        print("\nSales Orders:")
        print(json.dumps(sales, indent=2))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
