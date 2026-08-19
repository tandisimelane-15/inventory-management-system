# Inventory Management System

## Description
A Flask-based REST API for managing retail inventory, with CRUD operations, live product enrichment from the OpenFoodFacts API, and a CLI tool for interacting with the system without needing Postman or a browser.

## Features
- Full CRUD for inventory items (Create, Read, Update, Delete)
- Lookup product details (name, brand, ingredients) from OpenFoodFacts by barcode
- CLI tool to view, add, update, delete, and look up items
- In-memory mock database for simple local testing
- Error handling for missing items, bad input, and failed API calls
- Unit tests for routes, external API calls, and CLI commands (pytest + unittest.mock)

## How to run the Project
1. Clone the repository
```bash
   git clone https://github.com/<your-username>/inventory-management-system.git
   cd inventory-management-system
```
2. Create and activate a virtual environment
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies
```bash
   pip install -r requirements.txt
```
4. Run the Flask API
```bash
   python app.py
```
5. In a separate terminal (with venv activated), run the CLI
```bash
   python cli.py
```

## API Endpoints
| Method | Route | Description |
|---|---|---|
| GET | `/inventory` | Get all inventory items |
| GET | `/inventory/<id>` | Get a single item by ID |
| POST | `/inventory` | Create a new item |
| PATCH | `/inventory/<id>` | Update fields on an item |
| DELETE | `/inventory/<id>` | Delete an item |
| GET | `/lookup?barcode=<code>` | Fetch product details from OpenFoodFacts |

## Example CLI Usage

Run the CLI with the Flask server already running in another terminal:

    python cli.py

Then follow the prompts, for example adding a new item:

    1) View  2) Add  3) Update  4) Delete  5) Lookup  6) Quit
    Choose: 2
    Product name: Peanut Butter
    Price: 3.49
    Quantity: 40

## Running Tests
```bash
pytest
```

## Technologies Used
- Python
- Flask
- Requests
- Pytest / unittest.mock
- [OpenFoodFacts API v3.6](https://openfoodfacts.github.io/openfoodfacts-server/api/)
> **Note:** The `/lookup` route calls the OpenFoodFacts API (v3.6) with a custom `User-Agent` header, as required by their API usage guidelines. Read requests are rate-limited to 15/minute per IP by OpenFoodFacts.
## Future Implementations
- Persistent database (SQLite/Postgres) instead of in-memory storage
- Web-based admin UI in addition to CLI
- Auto-enrich new items from OpenFoodFacts on creation

## How to contribute
Pull requests are welcome. For major changes please open an issue first.

## License
MIT License

Copyright (c) 2026 Abigail Tandiwe

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact
- LinkedIn: [Abigail Tandiwe](https://www.linkedin.com/in/abigailtandi)
- Email: tandisimelane24@gmail.com