import unittest
from unittest.mock import Mock
from pycoupang.logistics import LogisticsAPI

class TestLogisticsAPI(unittest.TestCase):
    def setUp(self):
        self.client = Mock()
        self.logistics_api = LogisticsAPI(self.client)

    def test_create_shipping_location(self):
        location_data = {
            "vendorId": "test_vendor_id",
            "userId": "test_user_id",
            "shippingPlaceName": "Test_Shipping_Location",
            "global": "true",
            "usable": "true",
            "placeAddresses": [
                {
                    "addressType": "OVERSEA",
                    "countryCode": "US",
                    "companyContactNumber": "000-0000-0000",
                    "returnZipCode": "12345",
                    "returnAddress": "123 Main St",
                    "returnAddressDetail": ""
                }
            ],
            "remoteInfos": [{}]
        }
        self.client._request.return_value = {"success": True}

        response = self.logistics_api.create_shipping_location(location_data=location_data)

        self.client._request.assert_called_once_with("POST", 
            f"{self.logistics_api.VENDOR_ENDPOINT}/outboundShippingCenters", 
            json=location_data)
        self.assertEqual(response, {"success": True})

    def test_create_return_location(self):
        return_location_data = {
            "vendorId": "test_vendor_id", 
            "userId": "test_user_id",
            "shippingPlaceName": "Test_Return_Location",
            "goodsflowInfoOpenApiDto": {
                "deliverCode": "CJGLS",
                "deliveryCompanyName": "CJ Logistics",
                "contractNumber": "85500067",
                "contractCustomerNumber": "010-5464-6233",
                "vendorCreditFee05kg": "2500",
                "vendorCreditFee10kg": "2500",
                "vendorCreditFee20kg": "2500",
                "vendorCashFee05kg": "2500",
                "vendorCashFee10kg": "2500",
                "vendorCashFee20kg": "2500",
                "consumerCashFee05kg": "2500",
                "consumerCashFee10kg": "2500",
                "consumerCashFee20kg": "2500",
                "returnFee05kg": "2500",
                "returnFee10kg": "2500",
                "returnFee20kg": "2500"
            },
            "placeAddresses": [
                {
                    "addressType": "JIBUN",
                    "companyContactNumber": "010-5464-6233",
                    "returnZipCode": "112207",
                    "returnAddress": "경기도 파주시 탄현면 월롱산로",
                    "returnAddressDetail": "294-58"
                }
            ]
        }
        self.client._request.return_value = {"success": True}

        response = self.logistics_api.create_return_location(location_data=return_location_data)

        self.client._request.assert_called_once_with("POST", 
            f"{self.logistics_api.VENDOR_ENDPOINT}/returnShippingCenters", 
            json=return_location_data)
        self.assertEqual(response, {"success": True})

if __name__ == '__main__':
    unittest.main()