import json

from fastapi import Depends, APIRouter

from sqlalchemy import select, func, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.config import settings

from src.rating.models import Rating

from cryptography.fernet import Fernet


ENCRYPTION_KEY = bytes(settings.ENCRYPTION_KEY, 'utf-8')
fernet = Fernet(ENCRYPTION_KEY)

router = APIRouter(prefix='/rating',
                   tags=['rating'])


@router.get('/get_average_rating/{prod_id}')
async def get_average_rating(prod_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(func.avg(Rating.rating).label('average_rating')).where(Rating.prod_id == prod_id)
    result = await session.execute(stmt)
    result = result.first()
    response = {"average_rating": result.average_rating}

    return response


@router.post('/add_rating/{token}')
async def add_rating(token: str, session: AsyncSession = Depends(get_async_session)):
    try:
        # getting and transforming json string
        decrypted_json_bytes = fernet.decrypt(token.encode())
        json_str = json.loads(decrypted_json_bytes.decode())
        data = json.loads(json_str)
        # checking for a field in table
        stmt = select(Rating).filter(Rating.user_id == int(data["user_id"]), Rating.prod_id == int(data["prod_id"]))
        result = await session.execute(stmt)
        rating_field = result.scalar()
        # inserting rating
        if rating_field:
            stmt = delete(Rating).filter(Rating.user_id == int(data["user_id"]),
                                         Rating.prod_id == int(data["prod_id"]))
            await session.execute(stmt)

        stmt = insert(Rating).values(user_id=data["user_id"], rating=data["rating"], prod_id=data["prod_id"])
        result = await session.execute(stmt)
        response = {"msg": 'success',
                    "details": result}
        await session.commit()
    except Exception as exception:
        response = {"msg": 'fail',
                    "details": exception}

    return response
