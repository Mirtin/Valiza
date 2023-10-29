from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy import select, func

from database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession

from src.operations.models import Product


router = APIRouter(prefix="/operations",
                   tags=["operations"])


@router.get("/get_pages_count/")
async def get_pages_count(session: AsyncSession = Depends(get_async_session)):
    query = select(func.count(Product.id))
    result = await session.execute(query)
    result_list = []
    for row in result.all():
        result_list.append(row._mapping)

    response = {*result_list}
    return response


@router.get("/get_products/{skip}/{per_page}")
async def get_products(skip: int,
                       per_page: int,
                       session: AsyncSession = Depends(get_async_session)):
    query = select(Product.id,
                   Product.price,
                   Product.currency_code,
                   Product.discount,
                   Product.title,
                   Product.description,).limit(per_page).offset(skip)
    result = await session.execute(query)
    result_list = []
    for row in result.all():
        result_list.append(row._mapping)

    response = {"products": result_list}
    return response


@router.get("/get_product/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Product.id,
                   Product.price,
                   Product.currency_code,
                   Product.discount,
                   Product.title,
                   Product.description,
                   Product.category,).where(Product.id == product_id)
    result = await session.execute(query)
    result_list = []
    for row in result.all():
        result_list.append(row._mapping)

    response = {"product": result_list}

    return response
