import unittest
import os
from dotenv import load_dotenv
from pycoupang.client import CoupangClient
from pycoupang.category import CategoryAPI

class TestCategoryAPIIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        access_key = os.getenv('COUPANG_ACCESS_KEY')
        secret_key = os.getenv('COUPANG_SECRET_KEY')
        vendor_id = os.getenv('COUPANG_VENDOR_ID')
        cls.client = CoupangClient(access_key, secret_key, vendor_id)
        cls.category_api = CategoryAPI(cls.client)

    def test_get_category_meta(self):
        # Use a known valid category code for testing
        result = self.category_api.get_category_meta("83274")
        
        self.assertIn('data', result)
        self.assertIn('attributes', result['data'])
        self.assertIsInstance(result['data']['attributes'], list)

    def test_get_category_list(self):
        result = self.category_api.get_category_list()
        
        self.assertIn('data', result)
        self.assertIn('child', result['data'])
        self.assertIsInstance(result['data']['child'], list)
        self.assertGreater(len(result['data']['child']), 0)

    def test_get_category_details(self):
        # Use a known valid category code for testing
        result = self.category_api.get_category_details("83274")
        
        self.assertIn('data', result)
        self.assertIn('displayItemCategoryCode', result['data'])
        self.assertIsInstance(result['data']['name'], str)

if __name__ == '__main__':
    unittest.main()