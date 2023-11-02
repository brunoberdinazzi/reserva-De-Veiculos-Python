from app.database import get_db

def reserve_car(car_id: str):
    db = get_db()
    car = db.cars.find_one_and_update({"_id": car_id, "is_reserved": False}, {"$set": {"is_reserved": True}})
    if car is None:
        raise HTTPException(status_code=400, detail="Car is already reserved or not found")
    return {"message": "Car reserved successfully"}

def check_reservation(car_id: str):
    db = get_db()
    car = db.cars.find_one({"_id": car_id, "is_reserved": True})
    if car is None:
        return {"message": "Car is not reserved"}
    return {"message": "Car is reserved"}
