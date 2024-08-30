import unittest
from unittest.mock import Mock
from pycoupang.product import ProductAPI
from tests.mock_data.product_data import (
    CREATE_PRODUCT_DATA,
)

class TestProductAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.product_api = ProductAPI(self.mock_client)

    def test_create_product(self):
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.create(CREATE_PRODUCT_DATA)
        
        self.mock_client._request.assert_called_once_with(
            "POST", 
            self.product_api.BASE_ENDPOINT, 
            json=CREATE_PRODUCT_DATA
        )
        self.assertEqual(response["status_code"], 200)

    def test_get_product(self):
        product_id = "PROD123"
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.get(product_id)
        
        self.mock_client._request.assert_called_once_with(
            "GET", 
            f"{self.product_api.BASE_ENDPOINT}/{product_id}"
        )
        self.assertEqual(response["status_code"], 200)

    def test_request_approval(self):
        product_id = "PROD123"
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.request_approval(product_id)
        
        self.mock_client._request.assert_called_once_with(
            "PUT", 
            f"{self.product_api.BASE_ENDPOINT}/{product_id}/approvals"
        )
        self.assertEqual(response["status_code"], 200)

if __name__ == '__main__':
    unittest.main()