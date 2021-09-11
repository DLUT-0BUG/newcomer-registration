import logging
from mysql.connector import connect as MySQLConnect

from datamodel import StudentInfo


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnect(metaclass=Singleton):
    def __init__(self, host=None, port=3306, db=None, user=None, passwd=None):
        self.conn = MySQLConnect(
            host=host,
            port=port,
            database=db,
            user=user,
            password=passwd)

    def close(self):
        self.conn.close()

    def get_faculty(self):
        cursor = self.conn.cursor()
        query = """
            SELECT chinese_name 
            FROM faculty_list 
            WHERE id<100
        """
        cursor.execute(query)
        values = cursor.fetchall()
        faculties = []
        for i in values:
            faculties.append(i[0])
        cursor.close()
        return faculties

    def add_student_info(self, student: StudentInfo):
        cursor = self.conn.cursor()
        query = f"""
                    INSERT newcomer_info ()
                    VALUES ({student.to_value()});
                """
        logging.debug(f"add_student_info: query")
        cursor.execute(query)
        self.conn.commit()
        cursor.close()
