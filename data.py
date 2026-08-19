"""Mock in memory database for inventory items"""
INVENTORY = [
    {
        "Id" : 1,
        "barcode": "3017620422003",
        "product_name": "Nutella",
        "brands": "Ferrero",
        "ingredients_text": "Sugar, palm oil, hazelnuts...",
        "price": 4.99,
        "quantity": 25
    }
]

_next_id = 2

def get_all_items():
    return INVENTORY

def get_item_by_id(item_id):
    for item in INVENTORY:
        if item["id"] == item_id:
            return item
    return None

def create_item(data):
    global _next_id
    new_item = {
        "id": _next_id,
        "barcode": data.get("barcode"),
        "product_name": data.get("product_name"),
        "brands": data.get("brands"),
        "ingredients_text": data.get("ingredients_text"),
        "price": data.get("price"),
        "quantity": data.get("quantity"),
    }

    INVENTORY.append(new_item)
    _next_id += 1
    return new_item

def update_item(item_id, data):
    item = get_item_by_id(item_id)
    if item is None:
        return None
    for key in ("barcode", "product_name", "brands", "ingredients_text", "price", "quantity"):
        if key in data:
            item[key] = data[key]
    return item


def delete_item(item_id):
    item = get_item_by_id(item_id)
    if item is None:
        return False
    INVENTORY.remove(item)
    return True