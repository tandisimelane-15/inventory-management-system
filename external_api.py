"""Functions to query the OpenFoodFacts API."""
import requests

BASE_URL = "https://world.openfoodfacts.org"


def get_product_by_barcode(barcode):
    url = f"{BASE_URL}/api/v0/product/{barcode}.json"
    response = requests.get(url, timeout=5)
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