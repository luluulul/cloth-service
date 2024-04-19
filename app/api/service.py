import os
import httpx

SHOP_SERVICE_HOST_URL = 'http://localhost:8020/api/v1/shop/'

def is_shop_present(shop_id: int):
    return True