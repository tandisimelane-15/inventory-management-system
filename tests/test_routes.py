import pytest
from app import app
import data


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_data():
    data.INVENTORY.clear()
    data.INVENTORY.append({
        "id": 1, "barcode": "123", "product_name": "Nutella",
        "brands": "Ferrero", "ingredients_text": "Sugar...",
        "price": 4.99, "quantity": 25
    })
    data._next_id = 2


def test_get_all_items(client):
    res = client.get("/inventory")
    assert res.status_code == 200
    assert len(res.get_json()) == 1


def test_get_single_item(client):
    res = client.get("/inventory/1")
    assert res.status_code == 200
    assert res.get_json()["product_name"] == "Nutella"


def test_get_item_not_found(client):
    res = client.get("/inventory/999")
    assert res.status_code == 404


def test_create_item(client):
    res = client.post("/inventory", json={"product_name": "PB", "price": 3.5, "quantity": 10})
    assert res.status_code == 201
    assert res.get_json()["id"] == 2


def test_update_item(client):
    res = client.patch("/inventory/1", json={"price": 5.99})
    assert res.status_code == 200
    assert res.get_json()["price"] == 5.99


def test_delete_item(client):
    res = client.delete("/inventory/1")
    assert res.status_code == 204
    assert client.get("/inventory/1").status_code == 404