from typing import Optional

from fastapi import FastAPI, Form
from starlette import templating
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from datamodel import StudentInfo

app = FastAPI()
template = Jinja2Templates(directory="templates")

@app.get("/")
async def render_home(
    request: Request
):
    return template.TemplateResponse(
        "home.html",
        {
            "request": request 
        }
    )


@app.post("/register")
async def parse_form(
    request       : Request,
    name          : str = Form(...),
    gender        : str = Form(...),
    phone         : str = Form(...),
    faculty       : str = Form(...),
    class_        : str = Form(...),
    ideal_dept    : str = Form(...),
    sub_ideal_dept: str = Form(...),
    talent        : str = Form(...)
):
    register_info = StudentInfo(
        name=name,
        gender=gender,
        phone=phone,
        faculty=faculty,
        class_=class_,
        ideal_dept=ideal_dept,
        sub_ideal_dept=sub_ideal_dept,
        talent=talent
    )
    return {
        "status": 200,
        "msg": register_info
    }