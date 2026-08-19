"""Functions to query the OpenFoodFacts API."""
import requests

BASE_URL = "https://world.openfoodfacts.org"
HEADERS = {"User-Agent": "InventoryApp/1.0 (tandisimelane24@gmail.com)"}


def get_product_by_barcode(barcode):
    url = f"{BASE_URL}/api/v3.6/product/{barcode}.json"
    response = requests.get(url, headers=HEADERS, timeout=5)
    response.raise_for_status()
    result = response.json()

    if result.get("status") != 1:
        return None

    product = result.get("product", {})
    return {
        "barcode": barcode,
        "product_name": product.get("product_name"),
        "brands": product.get("brands"),
        "ingredients_text": product.get("ingredients_text"),
    }