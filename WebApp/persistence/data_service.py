import psycopg2
import os

from Models.Web.exercise import Exercise
from Models.Web.sub_exercise import SubExercise
from WebApp.persistence.settings import Settings


def get_connection():
    return psycopg2.connect(database=Settings.POSTGRES_DB,
                            user=Settings.POSTGRES_USER,
                            password=Settings.POSTGRES_PASSWORD,
                            host=Settings.POSTGRES_SERVER,
                            port=Settings.POSTGRES_PORT)


def execute_statement(sql_statement: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql_statement)
    conn.commit()
    conn.close()


def execute_statement_and_return(sql_statement: str) -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql_statement)
    elements = cur.fetchall()
    conn.close()

    return elements


def execute_command_if_table_is_empty(table_name: str, sql_statement: str) -> None:
    elements = execute_statement_and_return(f"SELECT 1 FROM {table_name}")

    if len(elements) == 0:
        execute_statement(sql_statement)


def get_all_elements(table_name: str) -> list:
    return execute_statement_and_return(f"SELECT * FROM {table_name}")


def get_all_elements_with_condition(table_name: str, column: str, value:str) -> list:
    return execute_statement_and_return(f"SELECT * FROM {table_name} WHERE {column}='{value}'")


class DataService:
    def __init__(self) -> None:
        self.file_directory = os.path.dirname(__file__)
        self.sql_directory = os.path.join(self.file_directory, "SQL")
        self.init_database()

    def init_database(self):
        with open(os.path.join(self.sql_directory, "init_postgres.sql")) as fs:
            execute_statement(fs.read())

        with open(os.path.join(self.sql_directory, "init_exercise_overview.sql")) as fs:
            execute_command_if_table_is_empty("exercises_overview", fs.read())

        with open(os.path.join(self.sql_directory, "init_exercise.sql")) as fs:
            execute_command_if_table_is_empty("sub_exercises", fs.read())

        print("Initialized Database")

    def get_list_of_exercises(self) -> list:
        rows = get_all_elements("exercises_overview")

        return [Exercise(row[1], row[2], row[3], row[4]) for row in rows]

    def get_list_of_sub_exercises(self, exercise: str) -> list:
        rows = get_all_elements_with_condition("sub_exercises", "exercise_type", exercise)

        return [SubExercise(row[1], row[2], row[3], row[4], row[5]) for row in rows]
