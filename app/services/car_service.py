from app.database import get_db
from app.models import Car

def create_car(car: Car):
    db = get_db()
    car_dict = car.dict()
    car_id = db.cars.insert_one(car_dict).inserted_id
    return {"car_id": str(car_id), **car_dict}

def get_cars(skip: int = 0):
    db = get_db()
    cars = list(db.cars.find().skip(skip))
    return cars