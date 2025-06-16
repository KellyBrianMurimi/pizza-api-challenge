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
python server/seed.py