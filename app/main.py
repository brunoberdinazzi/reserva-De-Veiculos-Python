from fastapi import FastAPI
from app.database import connect_to_mongodb
from app.routes import car, reservation

app = FastAPI()
app.include_router(car.router)
app.include_router(reservation.router)
