import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the vendor ID from the environment variable
VENDOR_ID = os.getenv('COUPANG_VENDOR_ID')

# Mock product data for testing
CREATE_PRODUCT_DATA = {
    "displayCategoryCode": 56137,
    "sellerProductName": "test_클렌징오일_관리용_상품명",
    "vendorId": VENDOR_ID,  # Use the environment variable here
    "saleStartedAt": "2017-11-30T00:00:00",
    "saleEndedAt": "2099-01-01T23:59:59",
    "displayProductName": "해피바스 솝베리 클렌징 오일",
    "brand": "해피바스",
    "generalProductName": "솝베리 클렌징 오일",
    "productGroup": "클렌징 오일",
    "deliveryMethod": "SEQUENCIAL",
    "deliveryCompanyCode": "KDEXP",
    "deliveryChargeType": "FREE",
    "deliveryCharge": 0,
    "freeShipOverAmount": 0,
    "deliveryChargeOnReturn": 2500,
    "remoteAreaDeliverable": "N",
    "unionDeliveryType": "UNION_DELIVERY",
    "returnCenterCode": "1000274592",
    "returnChargeName": "반품지_1",
    "companyContactNumber": "02-1234-678",
    "returnZipCode": "135-090",
    "returnAddress": "서울특별시 강남구 삼성동",
    "returnAddressDetail": "333",
    "returnCharge": 2500,
    "outboundShippingPlaceCode": "74010",
    "vendorUserId": "wing_loginId_123",
    "requested": True,
    "items": [
        {
            "itemName": "200ml_1개",
            "originalPrice": 13000,
            "salePrice": 10000,
            "maximumBuyCount": "100",
            "maximumBuyForPerson": "0",
            "outboundShippingTimeDay": "1",
            "maximumBuyForPersonPeriod": "1",
            "unitCount": 1,
            "adultOnly": "EVERYONE",
            "taxType": "TAX",
            "parallelImported": "NOT_PARALLEL_IMPORTED",
            "overseasPurchased": "NOT_OVERSEAS_PURCHASED",
            "pccNeeded": "false",
            "externalVendorSku": "0001",
            "barcode": "",
            "emptyBarcode": True,
            "emptyBarcodeReason": "상품확인불가_바코드없음사유",
            "modelNo": "171717",
            "extraProperties": {
                "coupangSalePrice": 5000,
                "onlineSalePriceForBooks": 10000,
                "transactionType": "manufacturer",
                "businessType": "Beauty"
            },
            "certifications": [
                {
                    "certificationType": "NOT_REQUIRED",
                    "certificationCode": ""
                }
            ],
            "searchTags": [
                "검색어1",
                "검색어2"
            ],
            "images": [
                {
                    "imageOrder": 0,
                    "imageType": "REPRESENTATION",
                    "vendorPath": "http://image11.coupangcdn.com/image/product/image/vendoritem/2018/06/25/3719529368/27a6b898-ff3b-4a27-b1e4-330a90c25e9c.jpg"
                },
                {
                    "imageOrder": 1,
                    "imageType": "DETAIL",
                    "vendorPath": "http://image11.coupangcdn.com/image/product/image/vendoritem/2017/02/21/3000169918/34b79649-d625-4f49-a260-b78bf7a573a8.jpg"
                },
                {
                    "imageOrder": 2,
                    "imageType": "DETAIL",
                    "vendorPath": "http://image11.coupangcdn.com/image/product/image/vendoritem/2018/06/28/3000169918/5716aa61-70bd-47cd-8f3d-f3d49e7f496d.jpg"
                }
            ],
            "notices": [
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "용량(중량)",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "제품 주요 사양",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "사용기한 또는 개봉 후 사용기간",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "사용방법",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "제조업자 및 제조판매업자",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "제조국",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "화장품법에 따라 기재, 표시하여야 하는 모든 성분",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "식품의약품안전처 심사 필 유무",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "사용할 때 주의사항",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "품질보증기준",
                    "content": "제품 이상 시 공정거래위원회 고시 소비자분쟁해결기준에 의거 보상합니다."
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "소비자상담관련 전화번호",
                    "content": "상세페이지 참조"
                }
            ],
            "attributes": [
                {
                    "attributeTypeName": "수량",
                    "attributeValueName": "1개"
                },
                {
                    "attributeTypeName": "개당 용량",
                    "attributeValueName": "200ml"
                }
            ],
            "contents": [
                {
                    "contentsType": "TEXT",
                    "contentDetails": [
                        {
                            "content": "<html><div></div><div><img src='http://image11.coupangcdn.com/image/product/content/vendorItem/2018/06/26/196713/738d905f-ed80-4fd8-ad21-ed87b195a19e.jpg' /><div></html>",
                            "detailType": "TEXT"
                        }
                    ]
                }
            ],
            "offerCondition": "NEW",
            "offerDescription": ""
        },
        {
            "itemName": "200ml_2개",
            "originalPrice": 26000,
            "salePrice": 20000,
            "maximumBuyCount": 100,
            "maximumBuyForPerson": 0,
            "outboundShippingTimeDay": 2,
            "maximumBuyForPersonPeriod": 1,
            "unitCount": 1,
            "adultOnly": "EVERYONE",
            "taxType": "TAX",
            "parallelImported": "NOT_PARALLEL_IMPORTED",
            "overseasPurchased": "NOT_OVERSEAS_PURCHASED",
            "pccNeeded": "false",
            "externalVendorSku": "0001",
            "barcode": "",
            "emptyBarcode": True,
            "emptyBarcodeReason": "상품확인불가_바코드없음사유",
            "modelNo": "171717",
            "extraProperties": {
                "coupangSalePrice": 5000,
                "onlineSalePriceForBooks": 10000,
                "transactionType": "manufacturer",
                "businessType": "Beauty"
            },
            "certifications": [
                {
                    "certificationType": "NOT_REQUIRED",
                    "certificationCode": ""
                }
            ],
            "searchTags": [
                "검색어1",
                "검색어2"
            ],
            "images": [
                {
                    "imageOrder": 0,
                    "imageType": "REPRESENTATION",
                    "vendorPath": "http://image11.coupangcdn.com/image/product/image/vendoritem/2018/06/26/3001519145/74100e2a-d1ad-4b50-9c78-840c12a3e10d.jpg"
                },
                {
                    "imageOrder": 1,
                    "imageType": "DETAIL",
                    "vendorPath": "http://image11.coupangcdn.com/image/product/image/vendoritem/2017/02/21/3000169918/34b79649-d625-4f49-a260-b78bf7a573a8.jpg"
                },
                {
                    "imageOrder": 2,
                    "imageType": "DETAIL",
                    "vendorPath": "http://image11.coupangcdn.com/image/product/image/vendoritem/2018/06/28/3000169918/5716aa61-70bd-47cd-8f3d-f3d49e7f496d.jpg"
                }
            ],
            "notices": [
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "용량(중량)",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "제품 주요 사양",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "사용기한 또는 개봉 후 사용기간",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "사용방법",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "제조업자 및 제조판매업자",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "제조국",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "화장품법에 따라 기재, 표시하여야 하는 모든 성분",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "식품의약품안전처 심사 필 유무",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "사용할 때 주의사항",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "품질보증기준",
                    "content": "상세페이지 참조"
                },
                {
                    "noticeCategoryName": "화장품",
                    "noticeCategoryDetailName": "소비자상담관련 전화번호",
                    "content": "상세페이지 참조"
                }
            ],
            "attributes": [
                {
                    "attributeTypeName": "수량",
                    "attributeValueName": "2개"
                },
                {
                    "attributeTypeName": "개당 용량",
                    "attributeValueName": "200ml"
                }
            ],
            "contents": [
                {
                    "contentsType": "TEXT",
                    "contentDetails": [
                        {
                            "content": "<html><div></div><div><img src='http://image11.coupangcdn.com/image/product/content/vendorItem/2018/06/26/196713/738d905f-ed80-4fd8-ad21-ed87b195a19e.jpg' /><div></html>",
                            "detailType": "TEXT"
                        }
                    ]
                }
            ],
            "offerCondition": "NEW",
            "offerDescription": ""
        }
    ],
    "requiredDocuments": [
        {
            "templateName": "기타인증서류",
            "vendorDocumentPath": "http://image11.coupangcdn.com/image/product/content/vendorItem/2018/07/02/41579010/eebc0c30-8f35-4a51-8ffd-808953414dc1.jpg"
        }
    ],
    "extraInfoMessage": "",
    "manufacture": "아모레퍼시픽"
}
