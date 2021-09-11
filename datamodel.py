from dataclasses import dataclass

@dataclass
class StudentInfo:
    name          : str
    gender        : str
    phone         : str
    faculty       : str
    class_        : str
    ideal_dept    : str
    sub_ideal_dept: str
    talent        : str

    class Config:
        orm_mode = True