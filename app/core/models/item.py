
from typing import Optional
from pydantic import Field
from datetime import datetime
from uuid import UUID
from .base import Base

class Item(Base):
    title: str
    quantity: int
    price: float
    sku: str
    product_id: UUID