from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class RegionName(str, Enum):
    north = 'north'
    south = 'south'
    east = 'east'
    west = 'west'
    center = 'center'


class BaseSale(BaseModel):
    date: date
    region: RegionName
    product: str
    unit_price: float
    quantity: int
    amount: float
    description: Optional[str]


class SaleCreate(BaseSale):
    pass

class SaleUpdate(BaseSale):
    pass


class Sale(BaseSale):
    id: int

    class Config:
        orm_mode = True
