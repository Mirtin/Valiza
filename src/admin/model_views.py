from sqladmin import ModelView

from src.operations.models import Product
from src.rating.models import Rating


class ProductModelView(ModelView, model=Product):
    pass


class RatingModelView(ModelView, model=Rating):
    pass

