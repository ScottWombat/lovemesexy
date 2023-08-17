from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
home_router = APIRouter()


@home_router.get("/menu",include_in_schema=False)
async def menu(request: Request):
   

    return templates.TemplateResponse("menu.html",{"request": request})

@home_router.get("/",include_in_schema=False)
async def intro(request: Request):
    client_host = request.client.host
    print(client_host)
    return templates.TemplateResponse("home.html",{"request": request})

@home_router.get("/main",include_in_schema=False)
async def menu(request: Request):
    menus =['Accessories', 'Anal Douches', 'Anal stimulators', 'Butt Plugs', 'Cock Rings', 'Penis Pumps', 'Prostate Massagers', 'Sex Dolls', 'Sex Machines', 'Sleeves & Extensions', 'Strokers', 'Urethral', 'Vibrating Masturbators']
    return templates.TemplateResponse("main.html",{"request": request,"menus": menus})

@home_router.get("/content",include_in_schema=False)
async def main_content(request: Request):
    return templates.TemplateResponse("content.html",{"request": request})

@home_router.get("/imgtb",include_in_schema=False)
async def main_content(request: Request):
    return templates.TemplateResponse("imgtb.html",{"request": request})