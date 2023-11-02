from fastapi import APIRouter, HTTPException, Query
from app.services.car_service import create_car, get_cars

router = APIRouter()

@router.post("/cars/")
async def create_car_endpoint(car: Car):
    return create_car(car)

@router.get("/cars/")
async def get_cars_endpoint(skip: int = Query(0, alias="skip")):
    return get_cars(skip)
