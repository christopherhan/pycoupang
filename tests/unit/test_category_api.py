import unittest
from unittest.mock import Mock, patch
from pycoupang.category import CategoryAPI

class TestCategoryAPI(unittest.TestCase):
    def setUp(self):
        self.mock_client = Mock()
        self.category_api = CategoryAPI(self.mock_client)

    def test_get_category_meta(self):
        mock_response = {"categoryMeta": "test_data"}
        self.mock_client._request.return_value = mock_response
        
        result = self.category_api.get_category_meta("12345")
        
        self.assertEqual(result, mock_response)
        self.mock_client._request.assert_called_once_with(
            "GET", 
            "/v2/providers/seller_api/apis/api/v1/marketplace/meta/category-related-metas/display-category-codes/12345"
        )

    @patch.object(CategoryAPI, '_process_kwargs')
    def test_get_category_list(self, mock_process_kwargs):
        mock_process_kwargs.return_value = {"param1": "value1"}
        mock_response = {"categories": ["category1", "category2"]}
        self.mock_client._request.return_value = mock_response
        
        result = self.category_api.get_category_list(param1="value1")
        
        self.assertEqual(result, mock_response)
        mock_process_kwargs.assert_called_once_with(param1="value1")
        self.mock_client._request.assert_called_once_with(
            "GET", 
            "/v2/providers/seller_api/apis/api/v1/marketplace/meta/display-categories",
            params={"param1": "value1"}
        )

    def test_get_category_details(self):
        mock_response = {"categoryDetails": "test_data"}
        self.mock_client._request.return_value = mock_response
        
        result = self.category_api.get_category_details("12345")
        
        self.assertEqual(result, mock_response)
        self.mock_client._request.assert_called_once_with(
            "GET", 
            "/v2/providers/seller_api/apis/api/v1/marketplace/meta/display-categories/12345"
        )

if __name__ == '__main__':
    unittest.main()