from fastapi import APIRouter, Response, Depends
from motor.motor_asyncio import AsyncIOMotorClient
#from app.core.dependencies import PermissionDependency, AllowAll
from app.core.db import get_db
import platform
import psutil
import asyncio
from app.core.services.product import ProductService
from app.core.models.product import Product
health_router = APIRouter()

@health_router.get("/api/health")
async def health(db: AsyncIOMotorClient = Depends(get_db)):
    try:
        # Check if the database is responsive
        await db.command('ping')
        db_status = 'up'
    except Exception:
        db_status = 'down'

    # Get system information
    system_info = {
        "system": platform.system(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict()
    }
    product= Product(name="ot")
  
    productservice = ProductService(db)
    p = await productservice.create(product)

    return {
        "database": db_status,
        "system_info": system_info
    }
