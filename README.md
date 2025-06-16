# Pizza Restaurant API 🍕

A RESTful API for managing pizza restaurants, their menus, and pizza associations built with Flask and SQLAlchemy.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Database Configuration](#database-configuration)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Validations](#validations)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Features
- RESTful endpoints for restaurants and pizzas
- Association management between restaurants and pizzas
- Data validations
- Proper error handling
- MVC architecture

## Setup

### Prerequisites
- Python 3.8+
- pipenv

### Installation
Go to https://github.comLinks to an external site.
Click New repository
Name your repo something like pizza-api-challenge
Keep it public (as advised)
Do not initialize with a README or .gitignore (you’ll do that locally)


## 🧱 Project Structure (MVC Preferred)
Follow the MVC (Model–View–Controller) pattern for structuring your application:
.
├── server/
│   ├── __init__.py
│   ├── app.py                # App setup
│   ├── config.py             # DB config, etc.
│   ├── models/               # 💾 Models (SQLAlchemy)
│   │   ├── __init__.py
│   │   └── restaurant.py
│   │   └── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/          # 🎯 Route handlers (Controllers)
│   │   ├── __init__.py
│   │   └── restaurant_controller.py
│   │   └── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   ├── seed.py               # Seed data
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md

## Create virtual environment and install dependencies:

pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

# Database Configuration
Initialize the database:

export FLASK_APP=server.app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed the database with sample data:
python -m server.seed

# Running the server:
flask run --port=5555

## API Endpoints
# Testing Instructions
Import the provided Postman collection (challenge-1-pizzas.postman_collection.json)

For each request:

In the Headers section, add:
Key: Content-Type
Value: application/json

For requests with bodies (POST), set the Body to:
Raw > JSON
Send the request and examine the response

Restaurants
Get All Restaurants
Method: GET
Endpoint: /restaurants
Description: Retrieve a list of all restaurants
Testing:

Select the "GET All Restaurants" request in Postman

Send the request

Expected Response (200 OK):

json
[
  {
    "id": 1,
    "name": "Pizza Place",
    "address": "123 Main St"
  }
]
Get Single Restaurant
Method: GET
Endpoint: /restaurants/<int:id>
Description: Get details of a specific restaurant including its pizzas
Testing:

Select the "GET Single Restaurant" request

Ensure the ID in the URL matches an existing restaurant

Send the request

Expected Response (200 OK):

json
{
  "id": 1,
  "name": "Pizza Place",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Tomato, Mozzarella, Pepperoni"
    }
  ]
}
Test with invalid ID to verify 404 response

Delete Restaurant
Method: DELETE
Endpoint: /restaurants/<int:id>
Description: Delete a restaurant and its associations
Testing:

Select the "DELETE Restaurant" request

Set the ID of an existing restaurant

Send the request

Expected Response: 204 No Content

Verify deletion by trying to GET the same ID

Pizzas
Get All Pizzas
Method: GET
Endpoint: /pizzas
Description: Retrieve a list of all available pizzas
Testing:

Select the "GET All Pizzas" request

Send the request

Expected Response (200 OK):

json
[
  {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Tomato, Mozzarella, Pepperoni"
  }
]
Restaurant Pizzas
Create Association
Method: POST
Endpoint: /restaurant_pizzas
Description: Create a new pizza-restaurant association
Testing:

Select the "POST RestaurantPizza" request

In the Body tab, provide valid JSON:

json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1
}
Send the request

Expected Success Response (201 Created):

json
{
  "id": 1,
  "price": 15,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Tomato, Mozzarella, Pepperoni"
  },
  "restaurant": {
    "id": 1,
    "name": "Pizza Place",
    "address": "123 Main St"
  }
}

# Test validation by sending:
Invalid price (should return 400)
Missing fields (should return 400)
Non-existent IDs (should return 404)


# Technologies Used
Python 3.8
Flask
SQLAlchemy
Flask-Migrate
Postman (for testing)

## License 
Copyright <2025> <Kelly Brian>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

