import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the vendor ID from the environment variable
VENDOR_ID = os.getenv('COUPANG_VENDOR_ID')
USER_ID = os.getenv('COUPANG_USER_ID')

SHIPPING_LOCATION_DATA = {
    "vendorId": VENDOR_ID,
    "userId": USER_ID,
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
    "remoteInfos": [
        {}
    ]
}

RETURN_LOCATION_DATA = {
    "vendorId": VENDOR_ID, 
    "userId": USER_ID,
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
