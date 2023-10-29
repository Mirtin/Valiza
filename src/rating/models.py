from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, CheckConstraint, Computed
from sqlalchemy.orm import declarative_base, DeclarativeMeta
from sqlalchemy_utils import ChoiceType

from src.operations.choices.symbols import SYMBOLS
from src.operations.choices.categories import CATEGORIES
from src.operations.models import Product

Base: DeclarativeMeta = declarative_base()


class Rating(Base):
    __tablename__ = "rating"
    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer)
    rating = Column("rating", Integer, CheckConstraint("rating > 0 AND rating < 6"))
    prod_id = Column("prod_id", ForeignKey(Product.id, ondelete="CASCADE"))