from typing import Optional
from pydantic import BaseModel, Field
from decimal import Decimal


class RatingValidator(BaseModel):
    amount: Optional[Decimal] = Field(ge=0.01, decimal_places=2)
