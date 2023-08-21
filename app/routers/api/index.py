from fastapi import APIRouter, Response, Depends

index_router = APIRouter()

@index_router.get("/api/home")
async def health():
    return {"message": "Hello World"}