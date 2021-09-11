import os
from typing import Optional
from dotenv import load_dotenv

from fastapi import FastAPI, Form
from starlette import templating
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from datamodel import StudentInfo
from database import DatabaseConnect

load_dotenv(verbose=True)
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_passwd = os.getenv('DB_PASSWORD')
DatabaseConnect(
    host=db_host,
    port=int(db_port),
    db=db_name,
    user=db_user,
    passwd=db_passwd)

app = FastAPI()
template = Jinja2Templates(directory="templates")


@app.get("/")
async def render_home(
    request: Request
):
    try:
        departments = DatabaseConnect().get_dept()
        faculties   = DatabaseConnect().get_faculty()
    except Exception as e:
        departments = []
        faculties = []
        error = True
        msg = f"系统出现错误，请联系老师。\n{e}"
    else:
        error = False
        msg = ""
    finally:
        return template.TemplateResponse(
            "home.html",
            {
                "request"    : request,
                "departments": departments,
                "faculties"  : faculties,
                "error"      : error,
                "msg"        : msg
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
    try:
        DatabaseConnect().add_student_info(register_info)
    except Exception as e:
        error = True
        msg = f"error occured\n{e}"
    else:
        error = False
        msg = "注册成功！"
    finally:
        return template.TemplateResponse(
            "results.html",
            {
                "request": request,
                "error": error,
                "msg": msg
            }
        )