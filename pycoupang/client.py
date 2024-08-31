import requests
import hmac
import hashlib
import base64
from datetime import datetime
import os
from .product import ProductAPI
from .logistics import LogisticsAPI

class CoupangClient:
    def __init__(self, access_key, secret_key, vendor_id, base_url=None):
        self.access_key = access_key
        self.secret_key = secret_key
        self.vendor_id = vendor_id
        self.base_url = base_url or os.getenv('COUPANG_BASE_URL', 'https://api-gateway.coupang.com')
        self.session = requests.Session()
        self.products = ProductAPI(self)
        self.logistics = LogisticsAPI(self)

    def _generate_signature(self, method, path, query_string=None):
        datetime_string = datetime.utcnow().strftime('%y%m%dT%H%M%SZ')

        message = datetime_string + method + path + (query_string or "")

        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        return f"CEA algorithm=HmacSHA256, access-key={self.access_key}, signed-date={datetime_string}, signature={signature}"

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        query_string = None

        if 'params' in kwargs:
            query_string = '&'.join([f"{k}={v}" for k, v in kwargs['params'].items()])

        authorization = self._generate_signature(method, f"/{endpoint}", query_string)

        headers = {
            "Content-type": "application/json;charset=UTF-8",
            "Authorization": authorization,
        }
        self.session.headers.update(headers)

        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()

    # ... rest of the methods (get, post, put, delete) remain the same ...

# Usage example
if __name__ == "__main__":
    base_url = os.environ.get('COUPANG_BASE_URL', 'https://api-gateway.coupang.com')
    access_key = os.environ.get('COUPANG_ACCESS_KEY')
    secret_key = os.environ.get('COUPANG_SECRET_KEY')
    vendor_id = os.environ.get('COUPANG_VENDOR_ID')

    if not all([base_url, access_key, secret_key, vendor_id]):
        raise ValueError("Missing required environment variables: COUPANG_BASE_URL, COUPANG_ACCESS_KEY, COUPANG_SECRET_KEY, COUPANG_VENDOR_ID")

    client = CoupangClient(base_url, access_key, secret_key, vendor_id)
    response = client.products.list_products(vendor_id=vendor_id)
    print(response)