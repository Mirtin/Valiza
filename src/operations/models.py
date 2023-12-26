from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, CheckConstraint, Computed
from sqlalchemy.orm import declarative_base, DeclarativeMeta
from sqlalchemy_utils import ChoiceType

from src.operations.choices.symbols import SYMBOLS
from src.operations.choices.categories import CATEGORIES


Base: DeclarativeMeta = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id = Column("id", Integer, primary_key=True)
    price = Column("price", DECIMAL(9, 2))
    currency_code = Column("currency_code", ChoiceType(SYMBOLS))
    discount = Column("discount", Integer)
    title = Column("title", String(length=100))
    description = Column("description", String(length=2500))
    category = Column("category", ChoiceType(CATEGORIES))
