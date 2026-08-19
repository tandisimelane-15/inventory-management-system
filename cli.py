"""CLI tool to interact with the inventory API."""
import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    r = requests.get(f"{BASE_URL}/inventory")
    print(r.json())


def add_item():
    product_name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    body = {"product_name": product_name, "price": price, "quantity": quantity}
    r = requests.post(f"{BASE_URL}/inventory", json=body)
    print(r.json())


def update_item():
    item_id = int(input("Item ID to update: "))
    price = input("New price (blank to skip): ")
    body = {}
    if price:
        body["price"] = float(price)
    r = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=body)
    print(r.json())


def delete_item():
    item_id = int(input("Item ID to delete: "))
    r = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print("Deleted" if r.status_code == 204 else r.json())


def lookup_item():
    barcode = input("Barcode: ")
    r = requests.get(f"{BASE_URL}/lookup", params={"barcode": barcode})
    print(r.json())


def main():
    actions = {
        "1": view_inventory,
        "2": add_item,
        "3": update_item,
        "4": delete_item,
        "5": lookup_item,
    }
    while True:
        print("\n1) View  2) Add  3) Update  4) Delete  5) Lookup  6) Quit")
        choice = input("Choose: ")
        if choice == "6":
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()