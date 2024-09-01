from typing import Dict, Any
from .base import BaseAPI

class CategoryAPI(BaseAPI):
    CATEGORY_META_ENDPOINT = "v2/providers/seller_api/apis/api/v1/marketplace/meta/category-related-metas/display-category-codes"
    DISPLAY_CATEGORIES_ENDPOINT = "v2/providers/seller_api/apis/api/v1/marketplace/meta/display-categories"

    def __init__(self, client):
        self.client = client
    
    def get_category_list(self, **kwargs) -> Dict[str, Any]:
        """
        Retrieve display category list.
        Coupang URL_API_NAME: None. View API documentation for details.

        Args:
            **kwargs: Optional parameters

        Returns:
            Dict[str, Any]: The response from the Coupang API containing category list information.
        """
        params = self._process_kwargs(**kwargs)
        return self.client._request("GET", self.DISPLAY_CATEGORIES_ENDPOINT, params=params)

    def get_category_meta(self, display_category_code: str) -> Dict[str, Any]:
        """
        Retrieve category metadata including notice, option, required documents, 
        certification information list, etc. 
        Coupang URL_API_NAME: None. View API documentation for details.

        Args:
            display_category_code (str): The display category code to retrieve metadata for.

        Returns:
            Dict[str, Any]: The response from the Coupang API containing category metadata.
        """
        endpoint = f"{self.CATEGORY_META_ENDPOINT}/{display_category_code}"
        return self.client._request("GET", endpoint)

    def get_category_details(self, display_category_code: str) -> Dict[str, Any]:
        """
        Retrieve detailed information for a specific display category.
        Coupang URL_API_NAME: None. View API documentation for details.

        Args:
            display_category_code (str): The display category code to retrieve details for.

        Returns:
            Dict[str, Any]: The response from the Coupang API containing category details.
        """
        endpoint = f"{self.DISPLAY_CATEGORIES_ENDPOINT}/{display_category_code}"
        return self.client._request("GET", endpoint)

