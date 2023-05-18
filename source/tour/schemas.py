from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel


class City(BaseModel):
    city_id: int
    city_name: str
    airport_id: int
    airport_name: str

    class Config:
        orm_mode = True

    pass


class Tour(BaseModel):
    tour_id: int
    tour_name: str
    city_from: str
    city_to: str
    airline_name: str
    flight_start: datetime
    flight_end: datetime
    flight_price: Decimal

    class Config:
        orm_mode = True

    pass
