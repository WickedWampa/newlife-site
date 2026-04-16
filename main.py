from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {
        "page_title": "New Life Sober Living"
    })


@app.get("/services", response_class=HTMLResponse)
def services(request: Request):
    return templates.TemplateResponse(request, "services.html", {
        "page_title": "Services | New Life Sober Living"
    })


@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request, sent: str | None = None):
    return templates.TemplateResponse(request, "contact.html", {
        "page_title": "Contact | New Life Sober Living",
        "sent": sent == "1"
    })


@app.post("/contact")
def contact_submit(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(""),
    message: str = Form(...)
):
    print("CONTACT FORM SUBMISSION")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Message:", message)
    return RedirectResponse(url="/contact?sent=1", status_code=303)