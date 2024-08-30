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
            self.product_api.SELLER_PRODUCTS_ENDPOINT, 
            json=CREATE_PRODUCT_DATA
        )
        self.assertEqual(response["status_code"], 200)

    def test_get_product(self):
        product_id = "PROD123"
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.get(product_id)
        
        self.mock_client._request.assert_called_once_with(
            "GET", 
            f"{self.product_api.SELLER_PRODUCTS_ENDPOINT}/{product_id}"
        )
        self.assertEqual(response["status_code"], 200)

    def test_request_approval(self):
        product_id = "PROD123"
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.request_approval(product_id)
        
        self.mock_client._request.assert_called_once_with(
            "PUT", 
            f"{self.product_api.SELLER_PRODUCTS_ENDPOINT}/{product_id}/approvals"
        )
        self.assertEqual(response["status_code"], 200)

    def test_delete_product(self):
        product_id = "PROD123"
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.delete(product_id)
        
        self.mock_client._request.assert_called_once_with(
            "DELETE", 
            f"{self.product_api.SELLER_PRODUCTS_ENDPOINT}/{product_id}"
        )
        self.assertEqual(response["status_code"], 200)

    def test_get_item_quantities(self):
        vendor_item_id = "ITEM1"
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.get_item_quantities(vendor_item_id)
        
        self.mock_client._request.assert_called_once_with(
            "GET", 
            f"{self.product_api.VENDOR_ITEMS_ENDPOINT}/{vendor_item_id}/inventories"
        )
        self.assertEqual(response["status_code"], 200)

    def test_get_product_summary(self):
        external_vendor_sku_code = "VENDOR_SKU_123"
        self.mock_client._request.return_value = {"status_code": 200}
        
        response = self.product_api.get_product_summary(external_vendor_sku_code)
        
        self.mock_client._request.assert_called_once_with(
            "GET", 
            f"{self.product_api.SELLER_PRODUCTS_ENDPOINT}/external-vendor-sku-codes/{external_vendor_sku_code}"
        )
        self.assertEqual(response["status_code"], 200)

    def test_list_products(self):
        vendor_id = "VENDOR123"
        self.mock_client._request.return_value = {"status_code": 200}
        
        # Test with only required parameter
        response = self.product_api.list_products(vendor_id=vendor_id)
        
        self.mock_client._request.assert_called_with(
            "GET", 
            self.product_api.SELLER_PRODUCTS_ENDPOINT,
            params={"vendorId": vendor_id}
        )
        self.assertEqual(response["status_code"], 200)

        # Test with all optional parameters
        response = self.product_api.list_products(
            vendor_id=vendor_id,
            next_token="NEXT_TOKEN",
            max_per_page=50,
            seller_product_id="PROD123",
            seller_product_name="Test Product",
            status="APPROVED",
            manufacture="Test Manufacturer",
            created_at="2023-05-01"
        )
        
        self.mock_client._request.assert_called_with(
            "GET", 
            self.product_api.SELLER_PRODUCTS_ENDPOINT,
            params={
                "vendorId": vendor_id,
                "nextToken": "NEXT_TOKEN",
                "maxPerPage": 50,
                "sellerProductId": "PROD123",
                "sellerProductName": "Test Product",
                "status": "APPROVED",
                "manufacture": "Test Manufacturer",
                "createdAt": "2023-05-01"
            }
        )
        self.assertEqual(response["status_code"], 200)

if __name__ == '__main__':
    unittest.main()