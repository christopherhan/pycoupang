from typing import Dict, Any


class ProductAPI:
    BASE_ENDPOINT = "v2/providers/seller_api/apis/api/v1/marketplace/seller-products"

    def __init__(self, client):
        self.client = client

    def create(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new product on Coupang Marketplace.

        Args:
            product_data (Dict[str, Any]): A dictionary containing the product information.

        Returns:
            Dict[str, Any]: The response from the Coupang API.
        """
        return self.client._request("POST", self.BASE_ENDPOINT, json=product_data)

    def get(self, product_id: str) -> Dict[str, Any]:
        """
        Retrieve a product from Coupang Marketplace by its ID.

        Args:
            product_id (str): The ID of the product to retrieve.

        Returns:
            Dict[str, Any]: The response from the Coupang API containing product information.
        """
        endpoint = f"{self.BASE_ENDPOINT}/{product_id}"
        return self.client._request("GET", endpoint)

    def request_approval(self, product_id: str) -> Dict[str, Any]:
        """
        Request approval for a product on Coupang Marketplace.

        Args:
            product_id (str): The ID of the product to request approval for.

        Returns:
            Dict[str, Any]: The response from the Coupang API.
        """
        endpoint = f"{self.BASE_ENDPOINT}/{product_id}/approvals"
        return self.client._request("PUT", endpoint)
