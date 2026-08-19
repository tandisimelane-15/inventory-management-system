from unittest.mock import patch, MagicMock
import cli


@patch("cli.requests.get")
def test_view_inventory(mock_get):
    mock_get.return_value = MagicMock(json=lambda: [{"id": 1, "product_name": "Nutella"}])
    cli.view_inventory()
    mock_get.assert_called_once()


@patch("cli.requests.delete")
def test_delete_item(mock_delete):
    mock_delete.return_value = MagicMock(status_code=204)
    with patch("builtins.input", return_value="1"):
        cli.delete_item()
    mock_delete.assert_called_once()