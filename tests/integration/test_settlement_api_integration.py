import unittest
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pycoupang.client import CoupangClient
from pycoupang.settlement import SettlementAPI

class TestSettlementAPIIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        access_key = os.getenv('COUPANG_ACCESS_KEY')
        secret_key = os.getenv('COUPANG_SECRET_KEY')
        vendor_id = os.getenv('COUPANG_VENDOR_ID')
        cls.client = CoupangClient(access_key, secret_key, vendor_id)
        cls.settlement_api = SettlementAPI(cls.client)
        cls.vendor_id = vendor_id

    def test_get_sales_detail(self):
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        
        result = self.settlement_api.get_sales_detail(
            vendor_id=self.vendor_id,
            recognition_date_from=start_date,
            recognition_date_to=end_date,
            token="",  # You might need to provide a valid token here
            max_per_page=50
        )
        
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)
        if len(result['data']) > 0:
            self.assertIn('orderId', result['data'][0])
            self.assertIn('amount', result['data'][0])

    def test_get_sales_detail_without_max_per_page(self):
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        
        result = self.settlement_api.get_sales_detail(
            vendor_id=self.vendor_id,
            recognition_date_from=start_date,
            recognition_date_to=end_date,
            token=""  # You might need to provide a valid token here
        )
        
        self.assertIn('data', result)
        self.assertIsInstance(result['data'], list)
        if len(result['data']) > 0:
            self.assertIn('orderId', result['data'][0])
            self.assertIn('amount', result['data'][0])

    def test_get_settlement_detail(self):
        current_date = datetime.now()
        revenue_recognition_year_month = current_date.strftime('%Y-%m')
        
        result = self.settlement_api.get_settlement_detail(
            revenue_recognition_year_month=revenue_recognition_year_month
        )
        
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()