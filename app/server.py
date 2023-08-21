from typing import List

from fastapi import FastAPI, Request, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
#from core.config import config
from app.core.cors import init_cors

from app.utils.initialize_routes import init_routers

from app.core.db import *


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        #dependencies=[Depends(Logging)],
        #middleware=make_middleware(),
    )
    '''
    app_.add_middleware(
    CORSMiddleware,
    allow_credentials = False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    )  
    '''
    app_.add_event_handler("startup", connect_and_init_db)
    app_.add_event_handler("shutdown", close_db_connect)

    app_.mount("/static", StaticFiles(directory="static"), name="static")
    init_cors(app_=app_)
    init_routers(app_=app_)
    #init_listeners(app_=app_)
    #init_cache()

    return app_

app = create_app()