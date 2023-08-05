import psycopg2
import os

from Models.Web.exercise_category import ExerciseCategory
from Models.Web.exercise_info import ExerciseInformation
from Models.Web.sub_exercise import SubExercise
from Models.exercise_info_dto import ExerciseInformationDto
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

        with open(os.path.join(self.sql_directory, "init_sub_exercise.sql")) as fs:
            execute_command_if_table_is_empty("sub_exercises", fs.read())

        with open(os.path.join(self.sql_directory, "init_exercise_information.sql")) as fs:
            execute_command_if_table_is_empty("exercise_information", fs.read())

        print("Initialized Database")

    def get_list_of_exercises(self) -> list:
        rows = get_all_elements("exercises_overview")

        return [ExerciseCategory(row[1], row[2], row[3], row[4]) for row in rows]

    def get_list_of_sub_exercises(self, exercise: str) -> list:
        rows = get_all_elements_with_condition("sub_exercises", "exercise_type", exercise)

        return [SubExercise(row[1], row[2], row[3], row[4], row[5]) for row in rows]

    def add_exercise_info(self, eidto: ExerciseInformationDto) -> None:
        add_ex_sql = "INSERT INTO exercise_repository(id, owner_id, exercise_type, sub_exercise_type, score, creation_epoch)" \
                     f"VALUES ({eidto.id}, '{eidto.owner_id}', '{eidto.exercise_type}', '{eidto.sub_exercise_type}', '', {eidto.creation_epoch});"

        execute_statement(add_ex_sql)

    def get_exercise_and_subtype(self, exercise_id: int) -> tuple:
        get_extype_subextype_sql = f"SELECT exercise_type, sub_exercise_type, score FROM exercise_repository WHERE id = {exercise_id}"

        rows = execute_statement_and_return(get_extype_subextype_sql)

        if len(rows) == 0:
            print(f"get_extype_subextype_sql for {exercise_id} could not be found")
            return None, None

        row = rows[0]

        return row[0], row[1], row[2]

    def get_exercise_info(self, exercise_id: int) -> ExerciseInformation:
        extype, subextype, score = self.get_exercise_and_subtype(exercise_id)

        get_ex_info_sql = f"SELECT * FROM exercise_information WHERE exercise_type = '{extype}' AND sub_exercise_type = '{subextype}'"

        rows = execute_statement_and_return(get_ex_info_sql)
        if len(rows) == 0:
            print(f"get_ex_info_sql for {exercise_id} could not be found")
            raise None

        row = rows[0]

        return ExerciseInformation(row[4], row[3].split(";"), row[6], score, subextype)

    def update_score(self, exercise_id: int, new_score: str) -> None:
        sql_update_score = f"UPDATE exercise_repository SET score = '{new_score}' WHERE id = '{exercise_id}'"

        execute_statement(sql_update_score)