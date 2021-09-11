import os
from typing import Optional

from fastapi import FastAPI, Form
from starlette import templating
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from datamodel import StudentInfo
from database import DatabaseConnect
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_passwd = os.getenv('DB_PASSWORD')
DatabaseConnect(
    host=db_host,
    port=db_port,
    db=db_name,
    user=db_user,
    passwd=db_passwd)

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
        id='1111111',
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
        "msg": register_info.to_value()
    }