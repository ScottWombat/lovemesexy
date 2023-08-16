from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from .base import Base

class Order(Base):
    total_price: float
    name: str
    line_items: List[Item]