from flask import Flask, request, jsonify
import data

app = Flask(__name__)


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(data.get_all_items()), 200


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    item = data.get_item_by_id(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@app.route("/inventory", methods=["POST"])
def add_inventory_item():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Request body must be JSON"}), 400
    if "price" not in body or "quantity" not in body:
        return jsonify({"error": "price and quantity are required"}), 400

    new_item = data.create_item(body)
    return jsonify(new_item), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Request body must be JSON"}), 400

    updated = data.update_item(item_id, body)
    if updated is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(updated), 200


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    deleted = data.delete_item(item_id)
    if not deleted:
        return jsonify({"error": "Item not found"}), 404
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)