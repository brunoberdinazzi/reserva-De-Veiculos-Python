from pydantic import BaseModel

class Car(BaseModel):
    make: str
    model: str
    year: int
    is_reserved: bool = False
    plate: str
    chassis: str
    owner: str
