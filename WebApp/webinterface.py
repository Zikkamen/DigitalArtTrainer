import os

from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from WebApp.art_evaluator_service import ArtEvaluatorService

app = FastAPI()

file_directory = os.path.dirname(__file__)
file_directory_persistence = os.path.join(file_directory, "persistence/files")
templates = Jinja2Templates(directory=os.path.join(file_directory, "resources/templates"))
app.mount("/static", StaticFiles(directory=os.path.join(file_directory, "resources/static")), name="static")

art_evaluator_service = ArtEvaluatorService()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/exercises", response_class=HTMLResponse)
async def read_exercises(request: Request):
    return templates.TemplateResponse("exercises_view.html",
                                      {
                                          "request": request,
                                          "exercise_list": art_evaluator_service.get_list_of_exercises()
                                      })


@app.get("/exercises/{exercise_name}", response_class=HTMLResponse)
async def read_sub_exercises(request: Request, exercise_name: str):
    return templates.TemplateResponse("sub_exercises_view.html",
                                      {
                                          "request": request,
                                          "sub_exercise_list": art_evaluator_service.get_list_of_sub_exercises(exercise_name)
                                      })


@app.get("/exercises/{exercise_name}/{sub_exercise_name}", response_class=RedirectResponse)
async def generate_exercise(request: Request, exercise_name: str, sub_exercise_name: str):
    print(exercise_name, sub_exercise_name)

    exercise_id = 1
    return f"/exercise/{exercise_id}"


@app.get("/exercise/{id}", response_class=HTMLResponse)
async def show_exercise(request: Request, id: int):
    return templates.TemplateResponse("exercise.html", {"request": request})


@app.post("/exercise/{id}", response_class=FileResponse)
async def process_exercise_request(id: int, task: Annotated[str, Form()]):
    print(task)
    return FileResponse(
        os.path.join(file_directory_persistence, f"{id}/task_1.png"),
        headers={'Content-Disposition': f'attachment; filename="{id}_task_1.png"'}
    )
