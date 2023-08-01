import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union

from WebApp.ArtEvaluatorService import ArtEvaluatorService
from WebApp.persistence.data_service import DataService

app = FastAPI()

file_directory = os.path.dirname(__file__)
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
                                          "exercise_list": art_evaluator_service.get_list_of_sub_exercises(exercise_name)
                                      })
