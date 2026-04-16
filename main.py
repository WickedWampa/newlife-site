from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/services", response_class=HTMLResponse)
def services(request: Request):
    return templates.TemplateResponse(request, "services.html")

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html")

@app.post("/contact")
def contact_submit(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    print(name, email, message)
    return {"status": "submitted"}