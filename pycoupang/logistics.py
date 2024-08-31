from typing import Dict, Any
import os
from .base import BaseAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LogisticsAPI(BaseAPI):

    VENDOR_ENDPOINT = f"v2/providers/openapi/apis/api/v4/vendors/{os.getenv('COUPANG_VENDOR_ID')}"

    def __init__(self, client, vendor_id=None):
        self.client = client

    def create_shipping_location(self, location_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new shipping location.
        Coupang URL_API_NAME: REGISTER_OUTBOUND_SHIPPING_CENTER

        Args:
            location_data (Dict[str, Any]): A dictionary containing the shipping location information.

        Returns:
            Dict[str, Any]: The response from the Coupang API.
        """
        endpoint = f"{self.VENDOR_ENDPOINT}/outboundShippingCenters"
        return self.client._request("POST", endpoint, json=location_data)

    def create_return_location(self, location_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new return location.
        Coupang URL_API_NAME: UPDATE_SHIPPING_CENTER_BY_VENDOR

        Args:
            return_location_data (Dict[str, Any]): A dictionary containing the return location information.

        Returns:
            Dict[str, Any]: The response from the Coupang API.
        """
        endpoint = f"{self.VENDOR_ENDPOINT}/returnShippingCenters"
        return self.client._request("POST", endpoint, json=location_data)
