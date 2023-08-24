from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
cart_router = APIRouter()



@cart_router.get("/cart",include_in_schema=False)
async def cart(request: Request):
    return templates.TemplateResponse("cart.html",{"request": request})