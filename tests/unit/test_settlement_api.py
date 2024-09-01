import unittest
from unittest.mock import Mock, patch
from pycoupang.settlement import SettlementAPI

class TestSettlementAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.settlement_api = SettlementAPI(self.mock_client)

    def test_get_sales_detail(self):
        mock_response = {"data": [{"orderId": "123", "amount": 1000}]}
        self.mock_client._request.return_value = mock_response
        
        result = self.settlement_api.get_sales_detail(
            vendor_id="VENDOR123",
            recognition_date_from="2023-01-01",
            recognition_date_to="2023-01-31",
            token="TOKEN123",
            max_per_page=50
        )
        
        self.assertEqual(result, mock_response)
        self.mock_client._request.assert_called_once_with(
            "GET", 
            "v2/providers/openapi/apis/api/v1/revenue-history",
            params={
                "vendorId": "VENDOR123",
                "recognitionDateFrom": "2023-01-01",
                "recognitionDateTo": "2023-01-31",
                "token": "TOKEN123",
                "maxPerPage": 50
            }
        )

    def test_get_sales_detail_without_max_per_page(self):
        mock_response = {"data": [{"orderId": "123", "amount": 1000}]}
        self.mock_client._request.return_value = mock_response
        
        result = self.settlement_api.get_sales_detail(
            vendor_id="VENDOR123",
            recognition_date_from="2023-01-01",
            recognition_date_to="2023-01-31",
            token="TOKEN123"
        )
        
        self.assertEqual(result, mock_response)
        self.mock_client._request.assert_called_once_with(
            "GET", 
            "v2/providers/openapi/apis/api/v1/revenue-history",
            params={
                "vendorId": "VENDOR123",
                "recognitionDateFrom": "2023-01-01",
                "recognitionDateTo": "2023-01-31",
                "token": "TOKEN123"
            }
        )

    @patch.object(SettlementAPI, '_process_kwargs')
    def test_get_settlement_detail(self, mock_process_kwargs):
        mock_process_kwargs.return_value = {
            "revenueRecognitionYearMonth": "2023-05"
        }
        mock_response = {"data": [{"settlementId": "456", "amount": 2000}]}
        self.mock_client._request.return_value = mock_response
        
        result = self.settlement_api.get_settlement_detail(
            revenue_recognition_year_month="2023-05"
        )
        
        self.assertEqual(result, mock_response)
        mock_process_kwargs.assert_called_once_with(
            revenueRecognitionYearMonth="2023-05"
        )
        self.mock_client._request.assert_called_once_with(
            "GET", 
            "v2/providers/marketplace_openapi/apis/api/v1/settlement-histories",
            params=mock_process_kwargs.return_value
        )

if __name__ == '__main__':
    unittest.main()