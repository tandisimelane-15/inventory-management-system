from unittest.mock import patch, MagicMock
import external_api


@patch("external_api.requests.get")
def test_get_product_by_barcode_found(mock_get):
    mock_get.return_value = MagicMock(status_code=200, json=lambda: {
        "status": 1,
        "product": {"product_name": "Nutella", "brands": "Ferrero", "ingredients_text": "Sugar"}
    })
    result = external_api.get_product_by_barcode("123")
    assert result["product_name"] == "Nutella"


@patch("external_api.requests.get")
def test_get_product_by_barcode_not_found(mock_get):
    mock_get.return_value = MagicMock(status_code=200, json=lambda: {"status": 0})
    result = external_api.get_product_by_barcode("000")
    assert result is None