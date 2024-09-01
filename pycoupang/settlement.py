from typing import Dict, Any
from .base import BaseAPI

class SettlementAPI(BaseAPI):
    SALES_DETAIL_ENDPOINT = "v2/providers/openapi/apis/api/v1/revenue-history"
    SETTLEMENT_DETAIL_ENDPOINT = "v2/providers/marketplace_openapi/apis/api/v1/settlement-histories"

    def __init__(self, client):
        self.client = client

    def get_sales_detail(self, vendor_id: str, recognition_date_from: str, 
                         recognition_date_to: str, token: str, 
                         max_per_page: int = None) -> Dict[str, Any]:
        """
        Retrieve sales detail information.
        Coupang URL_API_NAME: GET_REVENUE_HISTORY

        Args:
            vendor_id (str): The vendor ID
            recognition_date_from (str): Start date of the query period (YYYY-MM-DD)
            recognition_date_to (str): End date of the query period (YYYY-MM-DD)
            token (str): Token for the query
            max_per_page (int, optional): Maximum number of results per page

        Returns:
            Dict[str, Any]: The response from the Coupang API containing sales detail information.
        """
        params = {
            "vendorId": vendor_id,
            "recognitionDateFrom": recognition_date_from,
            "recognitionDateTo": recognition_date_to,
            "token": token
        }
        if max_per_page is not None:
            params["maxPerPage"] = max_per_page
        
        return self.client._request("GET", self.SALES_DETAIL_ENDPOINT, params=params)

    def get_settlement_detail(self, revenue_recognition_year_month: str) -> Dict[str, Any]:
        """
        Retrieve settlement detail information.
        Coupang URL_API_NAME: SETTLEMENT_HISTORIES

        Args:
            revenue_recognition_year_month (str): The year and month for revenue recognition (YYYY-MM)
            **kwargs: Additional optional parameters

        Returns:
            Dict[str, Any]: The response from the Coupang API containing settlement detail information.
        """
        params = self._process_kwargs(
            revenueRecognitionYearMonth=revenue_recognition_year_month, 
        )
        return self.client._request("GET", self.SETTLEMENT_DETAIL_ENDPOINT, params=params)