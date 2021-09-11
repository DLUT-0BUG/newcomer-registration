from typing import Optional

from fastapi import FastAPI, Form
from starlette import templating
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from datamodel import StudentInfo
from database import DatabaseConnect

app = FastAPI()
template = Jinja2Templates(directory="templates")
db = DatabaseConnect(
    host=,
    db=,
    user=,
    passwd=,
)


@app.get("/")
async def render_home(
    request: Request
):
    faculites = db.get_faculty()
    return template.TemplateResponse(
        "home.html",
        {
            "request": request,
            "faculties": faculites,
            "error": False,
            "err_msg": ""
        }
    )


@app.post("/register")
async def parse_form(
    request       : Request,
    name          : str = Form(...),
    id            : str = Form(...),
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
        id=id,
        gender=gender,
        phone=phone,
        faculty=faculty,
        class_=class_,
        ideal_dept=ideal_dept,
        sub_ideal_dept=sub_ideal_dept,
        talent=talent
    )
    db.add_student_info(register_info)
    return {
        "status": 200,
        "msg": register_info.to_value()
    }