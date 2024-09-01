import unittest
from pycoupang.base import BaseAPI

class TestBaseAPI(unittest.TestCase):

    def test_to_camel_case(self):
        self.assertEqual(BaseAPI._to_camel_case("test_string"), "testString")
        self.assertEqual(BaseAPI._to_camel_case("another_test_string"), "anotherTestString")
        self.assertEqual(BaseAPI._to_camel_case("already_camel"), "alreadyCamel")

    def test_process_kwargs(self):
        test_kwargs = {
            "next_token": "NEXT_TOKEN",
            "max_per_page": 50,
            "seller_product_id": "PROD123",
            "none_value": None
        }
        expected_result = {
            "nextToken": "NEXT_TOKEN",
            "maxPerPage": 50,
            "sellerProductId": "PROD123"
        }
        self.assertEqual(BaseAPI._process_kwargs(**test_kwargs), expected_result)

if __name__ == '__main__':
    unittest.main()