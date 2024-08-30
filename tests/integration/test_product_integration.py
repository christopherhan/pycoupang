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

    @classmethod
    def tearDownClass(cls):
        # Here you could add logic to delete the created product if needed
        pass

if __name__ == '__main__':
    unittest.main()