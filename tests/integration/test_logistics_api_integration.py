import unittest
import os
from pycoupang.client import CoupangClient
from pycoupang.logistics import LogisticsAPI
from tests.mock_data.location_data import SHIPPING_LOCATION_DATA, RETURN_LOCATION_DATA_DOMESTIC

class TestLogisticsAPIIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.access_key = os.getenv('COUPANG_ACCESS_KEY')
        cls.secret_key = os.getenv('COUPANG_SECRET_KEY')
        cls.vendor_id = os.getenv('COUPANG_VENDOR_ID')

        if not all([cls.access_key, cls.secret_key, cls.vendor_id]):
            raise ValueError("Missing required environment variables")

        cls.client = CoupangClient(cls.access_key, cls.secret_key, cls.vendor_id)
        cls.logistics_api = cls.client.logistics

    def test_create_shipping_location_integration(self):
        response = self.logistics_api.create_shipping_location(SHIPPING_LOCATION_DATA)
        self.assertIn("success", response)

    def test_create_return_location_integration(self):
        response = self.logistics_api.create_return_location(RETURN_LOCATION_DATA_DOMESTIC)
        self.assertIn("success", response)

if __name__ == '__main__':
    unittest.main()