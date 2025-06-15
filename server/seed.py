from app import create_app, db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

app = create_app()
with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()

    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="BBQ Chicken", ingredients="Chicken, BBQ Sauce, Cheese")

    r1 = Restaurant(name="Pizza Inn", address="Nairobi")
    r2 = Restaurant(name="The Paz", address="address3")

    db.session.add_all([p1, p2, r1, r2])
    db.session.commit()

    rp1 = RestaurantPizza(price=5, pizza_id=p1.id, restaurant_id=r2.id)
    db.session.add(rp1)
    db.session.commit()

    print("Database seeded!")
