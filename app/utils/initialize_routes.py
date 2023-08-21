from fastapi import FastAPI
from app.routers.web.home import home_router
from app.routers.api.health import health_router
from app.routers.api.index import index_router
def init_routers(app_: FastAPI) -> None:
    app_.include_router(home_router)
    app_.include_router(health_router)
    app_.include_router(index_router)

