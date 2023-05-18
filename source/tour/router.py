from fastapi import APIRouter, Depends, HTTPException
from typing import List

from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from database import get_async_session

from tour.models import city_model, tour_model
from tour.schemas import City, Tour

router = APIRouter()


@router.post('/add_city')
async def add_city(
        new_city: City,
        session: AsyncSession = Depends(get_async_session)):
    stmt = (
        insert(city_model).
        values(**new_city.dict())
    )
    try:
        await session.execute(stmt)
    except Exception:
        await session.rollback()
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': 'Something went wrong'
        })

    await session.commit()
    return {
        'status': 'success',
        'data': None
    }


@router.post('/add_tour')
async def add_tour(
        new_tour: Tour,
        session: AsyncSession = Depends(get_async_session)):
    stmt = (
        insert(tour_model).
        values(**new_tour.dict())
    )
    try:
        await session.execute(stmt)
    except Exception:
        await session.rollback()
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': 'Something went wrong'
        })

    await session.commit()
    return {
        'status': 'success',
        'data': None
    }


@router.get('/get_tour/{id}', response_model=List[Tour])
@cache(expire=60)
async def get_tour(
        id: int,
        session: AsyncSession = Depends(get_async_session)) -> List[Tour]:

    query = select(tour_model).where(tour_model.c.tour_id == id)
    try:
        result = await session.execute(query)
        tours = result.all()
        return [Tour(
            tour_id=tour.tour_id,
            tour_name=tour.tour_name,
            city_from=tour.city_from,
            city_to=tour.city_to,
            airline_name=tour.airline_name,
            flight_start=tour.flight_start,
            flight_end=tour.flight_end,
            flight_price=tour.flight_price
        ) for tour in tours]
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status:': Exception,
            'data': None,
            'details': 'Something went wrong'
        })


