from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class Base(BaseModel):
    id: UUID
    create_time: datetime
    update_time: datetime
    deleted: bool