from datetime import datetime

from sqlalchemy import Table, Column, JSON, Integer, String, DECIMAL, TIMESTAMP, ForeignKey, Boolean
from database import metadata


city_model = Table(
    'city',
    metadata,
    Column('city_id', Integer, primary_key=True, nullable=False),
    Column('city_name', String, unique=True, nullable=False),
    Column('airport_id', Integer, unique=True, nullable=False),
    Column('airport_name', String, unique=True, nullable=False)
)

airport_schedule_model = Table(
    'airport_schedule',
    metadata,
    Column('flight_date', TIMESTAMP(timezone=True)),
    Column('city_from', String),
    Column('city_to', String),
    Column('airport_from', String),
    Column('airport_to', String),

)


tour_model = Table(
    'tour',
    metadata,
    Column('tour_id', Integer, primary_key=True),
    Column('tour_name', String, nullable=False),
    Column('city_from', String, nullable=False),
    Column('city_to', String, nullable=False),
    Column('airline_name', String),
    Column('flight_start', TIMESTAMP(timezone=True)),
    Column('flight_end', TIMESTAMP(timezone=True)),
    Column('flight_price', DECIMAL)

)