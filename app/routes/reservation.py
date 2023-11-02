from fastapi import APIRouter
from app.services.reservation_service import reserve_car, check_reservation

router = APIRouter()

@router.put("/cars/{car_id}/reserve")
async def reserve_car_endpoint(car_id: str):
    return reserve_car(car_id)

@router.get("/cars/{car_id}/check-reservation")
async def check_reservation_endpoint(car_id: str):
    return check_reservation(car_id)
