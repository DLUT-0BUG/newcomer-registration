from dataclasses import dataclass

@dataclass
class StudentInfo:
    name          : str
    id            : str
    gender        : str
    gender_additional = ""
    phone         : str
    faculty       : str
    major         = ""
    class_        : str
    ideal_dept    : str
    sub_ideal_dept: str
    talent        : str

    class Config:
        orm_mode = True

    def to_value(self):
        return ",".join(
            list(map(
                lambda x: f"'{x}'",
                [self.name, self.id, self.gender, self.gender_additional, self.phone, self.faculty, self.major,
                 self.class_, self.ideal_dept, self.sub_ideal_dept, self.talent]
            ))
        )
