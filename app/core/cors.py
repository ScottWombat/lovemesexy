from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]


def init_cors(app_: FastAPI) -> None:
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
