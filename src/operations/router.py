import json

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.operations.models import Product

router = APIRouter(prefix="/operations",
                   tags=["operations"])


@router.get("/get_pages_count/")
async def get_pages_count(session: AsyncSession = Depends(get_async_session)):
    query = select(func.count(Product.id))
    result = await session.execute(query)
    result = result.first()

    response = {"count": result.count}

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
                   Product.description,
                   Product.category).limit(per_page).offset(skip)
    result = await session.execute(query)
    response = {}
    # using enumerate for unique product key in response dict
    for index, item in enumerate(result):
        data = {"id": item.id,
                "price": str(item.price),
                "currency_code": str(item.currency_code),
                "discount": item.discount,
                "title": item.title,
                "description": item.description,
                "category": str(item.category)}
        response[f"product{index}"] = data

    return response


@router.get("/get_product/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(Product.id,
                  Product.price,
                  Product.currency_code,
                  Product.discount,
                  Product.title,
                  Product.description,
                  Product.category).where(Product.id == product_id)
    result = await session.execute(stmt)
    result = result.first()
    response = {"id": result.id,
                "price": result.price,
                "currency_code": result.currency_code,
                "discount": result.discount,
                "title": result.title,
                "description": result.description,
                "category": result.category}

    return response
