from server.app import create_app
from server.db import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("Deleting existing data...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    print("Seeding restaurants...")
    r1 = Restaurant(name="Pizza Place", address="123 Main St, Nairobi")
    r2 = Restaurant(name="The Paz", address="456 Flavor Ave, Nairobi")

    print("Seeding pizzas...")
    p1 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p2 = Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Ham, Pineapple")
    p3 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")

    db.session.add_all([r1, r2, p1, p2, p3])
    db.session.commit()

    print("Seeding restaurant pizzas...")
    # Changed prices to be between 1-30
    rp1 = RestaurantPizza(price=15, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=20, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Seeding complete!")