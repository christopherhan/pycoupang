# PyCoupang

PyCoupang is a Python client library for the Coupang WING API. It provides a simple interface to interact with Coupang's API endpoints.

## Installation

Install PyCoupang using pip:

```bash
pip install python-coupang
```

## Usage

To use the PyCoupang library, you need to set up your environment with the necessary credentials. You can get these credentials by registering an application on the [Coupang Developer Portal](https://developers.coupangcorp.com/hc/ko/articles/20288952179993-OpenAPI-Key-%EB%B0%9C%EA%B8%89%EB%B0%9B%EA%B8%B0).

Once you have your credentials, you can set them as environment variables:

```bash
export COUPANG_ACCESS_KEY=<your_access_key>
export COUPANG_SECRET_KEY=<your_secret_key>
export COUPANG_VENDOR_ID=<your_vendor_id>
```

Alternatively, you can create a `.env` file in your project root with these variables:

```bash
COUPANG_ACCESS_KEY=<your_access_key>
COUPANG_SECRET_KEY=<your_secret_key>
COUPANG_VENDOR_ID=<your_vendor_id>
```


Then, you can use the library in your Python code:


```python
import os
from dotenv import load_dotenv
from pycoupang.client import CoupangClient

# load environment variables
load_dotenv()

client = CoupangClient(
    access_key=os.getenv('COUPANG_ACCESS_KEY'),
    secret_key=os.getenv('COUPANG_SECRET_KEY'),
    vendor_id=os.getenv('COUPANG_VENDOR_ID')
)
# list products
response = client.products.list_products(vendor_id=os.getenv('COUPANG_VENDOR_ID'))

# get a specific product
response = client.products.get("product_id")

# create a new product
new_product_data = {
    # Your product data here
}
response = client.products.create(new_product_data)
```

