import unittest
import os
from dotenv import load_dotenv
from pycoupang.client import CoupangClient
from tests.mock_data.product_data import CREATE_PRODUCT_DATA

class TestProductAPIIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        base_url = os.getenv('COUPANG_BASE_URL', 'https://api-gateway.coupang.com')
        access_key = os.getenv('COUPANG_ACCESS_KEY')
        secret_key = os.getenv('COUPANG_SECRET_KEY')
        vendor_id = os.getenv('COUPANG_VENDOR_ID')

        if not all([base_url, access_key, secret_key, vendor_id]):
            raise ValueError("Missing required environment variables")

        cls.client = CoupangClient(base_url, access_key, secret_key, vendor_id)
        cls.created_product_id = None

    def assert_success_response(self, response, message=""):
        try:
            self.assertIn('code', response, f"Response does not contain 'code' key. {message}")
            self.assertEqual(response['code'], 'SUCCESS', f"Response code is not 'SUCCESS'. {message}")
        except AssertionError as e:
            print(f"API Response: {response}")
            raise e

    def test_01_create_product(self):
        response = self.client.products.create(CREATE_PRODUCT_DATA)
        self.assert_success_response(response, "Failed to create product")
        self.assertIn('data', response, "Response does not contain 'data' key")
        self.assertIn('productId', response['data'], "Response data does not contain 'productId'")
        TestProductAPIIntegration.created_product_id = response['data']['productId']

    def test_02_get_product(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        response = self.client.products.get(TestProductAPIIntegration.created_product_id)
        self.assert_success_response(response, f"Failed to get product {TestProductAPIIntegration.created_product_id}")

    def test_03_request_approval(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        response = self.client.products.request_approval(TestProductAPIIntegration.created_product_id)
        self.assert_success_response(response, f"Failed to request approval for product {TestProductAPIIntegration.created_product_id}")

    def test_04_get_item_quantities(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        
        vendor_item_id = TestProductAPIIntegration.created_product_id
        response = self.client.products.get_item_quantities(vendor_item_id)
        
        self.assert_success_response(response, f"Failed to get item quantities for {vendor_item_id}")
        self.assertIn('data', response, "Response does not contain 'data' key")
        self.assertIn('items', response['data'], "Response data does not contain 'items'")
        self.assertGreater(len(response['data']['items']), 0, "No items returned")

    def test_05_get_product_summary(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        
        external_vendor_sku_code = CREATE_PRODUCT_DATA['items'][0]['externalVendorSku']
        
        response = self.client.products.get_product_summary(external_vendor_sku_code)
        
        self.assert_success_response(response, f"Failed to get product summary for {external_vendor_sku_code}")
        self.assertIn('data', response, "Response does not contain 'data' key")

    def test_06_list_products(self):
        vendor_id = os.getenv('COUPANG_VENDOR_ID')
        if not vendor_id:
            self.skipTest("COUPANG_VENDOR_ID not set in environment variables")
        
        response = self.client.products.list_products(
            vendor_id=vendor_id,
            maxPerPage=10
        )
        
        self.assert_success_response(response, f"Failed to list products for vendor {vendor_id}")
        self.assertIn('data', response, "Response does not contain 'data' key")
        self.assertIn('products', response['data'], "Response data does not contain 'products'")
        self.assertLessEqual(len(response['data']['products']), 10, "More than 10 products returned")

    def test_07_delete_product(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        response = self.client.products.delete(TestProductAPIIntegration.created_product_id)
        self.assert_success_response(response, f"Failed to delete product {TestProductAPIIntegration.created_product_id}")
        TestProductAPIIntegration.created_product_id = None

    @classmethod
    def tearDownClass(cls):
        if cls.created_product_id:
            try:
                cls.client.products.delete(cls.created_product_id)
            except Exception as e:
                print(f"Failed to delete product {cls.created_product_id} in teardown: {e}")

if __name__ == '__main__':
    unittest.main()