from typing import Dict, Any, List, Optional


class ProductAPI:
    SELLER_PRODUCTS_ENDPOINT = "v2/providers/seller_api/apis/api/v1/marketplace/seller-products"
    VENDOR_ITEMS_ENDPOINT = "v2/providers/seller_api/apis/api/v1/marketplace/vendor-items"

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
        return self.client._request("POST", self.SELLER_PRODUCTS_ENDPOINT, json=product_data)

    def get(self, product_id: str) -> Dict[str, Any]:
        """
        Retrieve a product from Coupang Marketplace by its ID.

        Args:
            product_id (str): The ID of the product to retrieve.

        Returns:
            Dict[str, Any]: The response from the Coupang API containing product information.
        """
        endpoint = f"{self.SELLER_PRODUCTS_ENDPOINT}/{product_id}"
        return self.client._request("GET", endpoint)

    def request_approval(self, product_id: str) -> Dict[str, Any]:
        """
        Request approval for a product on Coupang Marketplace.

        Args:
            product_id (str): The ID of the product to request approval for.

        Returns:
            Dict[str, Any]: The response from the Coupang API.
        """
        endpoint = f"{self.SELLER_PRODUCTS_ENDPOINT}/{product_id}/approvals"
        return self.client._request("PUT", endpoint)

    def delete(self, product_id: str) -> Dict[str, Any]:
        """
        Delete a product from Coupang Marketplace.

        Args:
            product_id (str): The ID of the product to delete.

        Returns:
            Dict[str, Any]: The response from the Coupang API.
        """
        endpoint = f"{self.SELLER_PRODUCTS_ENDPOINT}/{product_id}"
        return self.client._request("DELETE", endpoint)

    def get_item_quantities(self, vendor_item_id: str) -> Dict[str, Any]:
        """
        Query quantity, price, and status for a single product item.

        Args:
            vendor_item_id (str): The vendor item ID to query.

        Returns:
            Dict[str, Any]: The response from the Coupang API containing item information.
        """
        endpoint = f"{self.VENDOR_ITEMS_ENDPOINT}/{vendor_item_id}/inventories"
        return self.client._request("GET", endpoint)

    def get_product_summary(self, external_vendor_sku_code: str) -> Dict[str, Any]:
        """
        Query a summary of product info by external vendor SKU code.

        Args:
            external_vendor_sku_code (str): The external vendor SKU code of the product.

        Returns:
            Dict[str, Any]: The response from the Coupang API containing product summary information.
        """
        endpoint = f"{self.SELLER_PRODUCTS_ENDPOINT}/external-vendor-sku-codes/{external_vendor_sku_code}"
        return self.client._request("GET", endpoint)

    def list_products(self, vendor_id: str, **kwargs) -> Dict[str, Any]:
        """
        Query a list of products with paging.

        Args:
            vendor_id (str): The vendor ID.
            **kwargs: Optional parameters (nextToken, maxPerPage, sellerProductId, 
                      sellerProductName, status, manufacture, createdAt)

        Returns:
            Dict[str, Any]: The response from the Coupang API containing the list of products.
        """
        params = {"vendorId": vendor_id, **{k: v for k, v in kwargs.items() if v is not None}}
        return self.client._request("GET", self.SELLER_PRODUCTS_ENDPOINT, params=params)
