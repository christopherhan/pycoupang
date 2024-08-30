import requests
import hmac
import hashlib
import base64
from datetime import datetime
import os
from .product import ProductAPI

class CoupangClient:
    def __init__(self, base_url, access_key, secret_key, vendor_id):
        self.base_url = base_url
        self.access_key = access_key
        self.secret_key = secret_key
        self.session = requests.Session()

        self.products = ProductAPI(self)

    def _generate_signature(self, method, path, timestamp):
        message = f"{method}\n{path}\n{timestamp}"
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).digest()
        return base64.b64encode(signature).decode('utf-8')

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        signature = self._generate_signature(method, f"/{endpoint}", timestamp)

        headers = {
            "X-COUPANG-ACCESS-KEY": self.access_key,
            "X-COUPANG-TIMESTAMP": timestamp,
            "X-COUPANG-SIGNATURE": signature,
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
    response = client.get("users")
    print(response)