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

    def test_01_create_product(self):
        response = self.client.products.create(CREATE_PRODUCT_DATA)
        self.assertIn('code', response)
        self.assertEqual(response['code'], 'SUCCESS')
        self.assertIn('data', response)
        self.assertIn('productId', response['data'])
        TestProductAPIIntegration.created_product_id = response['data']['productId']

    def test_02_get_product(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        response = self.client.products.get(TestProductAPIIntegration.created_product_id)
        self.assertIn('code', response)
        self.assertEqual(response['code'], 'SUCCESS')

    def test_03_request_approval(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        response = self.client.products.request_approval(TestProductAPIIntegration.created_product_id)
        self.assertIn('code', response)
        self.assertEqual(response['code'], 'SUCCESS')

    def test_04_delete_product(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        response = self.client.products.delete(TestProductAPIIntegration.created_product_id)
        self.assertIn('code', response)
        self.assertEqual(response['code'], 'SUCCESS')
        TestProductAPIIntegration.created_product_id = None

    def test_05_get_item_quantities(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        
        # Assuming the created_product_id is also the vendor_item_id
        vendor_item_id = TestProductAPIIntegration.created_product_id
        response = self.client.products.get_item_quantities(vendor_item_id)
        
        self.assertIn('code', response)
        self.assertEqual(response['code'], 'SUCCESS')
        self.assertIn('data', response)
        self.assertIn('items', response['data'])
        self.assertGreater(len(response['data']['items']), 0)

    def test_06_get_product_summary(self):
        if not TestProductAPIIntegration.created_product_id:
            self.skipTest("No product created to test")
        
        # Assuming we can get the external_vendor_sku_code from the created product
        # You might need to adjust this based on how you're storing or retrieving this information
        external_vendor_sku_code = "VENDOR_SKU_123"  # Replace with actual code if available
        
        response = self.client.products.get_product_summary(external_vendor_sku_code)
        
        self.assertIn('code', response)
        self.assertEqual(response['code'], 'SUCCESS')
        self.assertIn('data', response)
        # Add more specific assertions based on the expected response structure

    def test_07_list_products(self):
        vendor_id = os.getenv('COUPANG_VENDOR_ID')
        if not vendor_id:
            self.skipTest("COUPANG_VENDOR_ID not set in environment variables")
        
        response = self.client.products.list_products(
            vendor_id=vendor_id,
            max_per_page=10
        )
        
        self.assertIn('code', response)
        self.assertEqual(response['code'], 'SUCCESS')
        self.assertIn('data', response)
        self.assertIn('products', response['data'])
        self.assertLessEqual(len(response['data']['products']), 10)

    @classmethod
    def tearDownClass(cls):
        if cls.created_product_id:
            try:
                cls.client.products.delete(cls.created_product_id)
            except Exception as e:
                print(f"Failed to delete product {cls.created_product_id} in teardown: {e}")

if __name__ == '__main__':
    unittest.main()