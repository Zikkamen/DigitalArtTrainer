import os
from typing import Annotated

from PIL import Image
from fastapi import FastAPI, Request, Form, HTTPException, status, UploadFile, File
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
    return templates.TemplateResponse("index.html",
                                      {
                                          "request": request,
                                          "exercise_list": art_evaluator_service.get_list_of_exercises()
                                      })


@app.get("/exercises", response_class=HTMLResponse)
async def read_exercises(request: Request):
    return templates.TemplateResponse("exercises_overview.html",
                                      {
                                          "request": request,
                                          "page_name": "Exercises Overview",
                                          "exercise_list": art_evaluator_service.get_list_of_exercises(),
                                          "bread_crumb_list": [(request.url_for("read_root"), "Home"),
                                                               (request.url_for("read_exercises"), "Exercises")]
                                      })


@app.get("/exercises/{exercise_name}", response_class=HTMLResponse)
async def read_sub_exercises(request: Request, exercise_name: str):
    return templates.TemplateResponse("sub_exercises_view.html",
                                      {
                                          "request": request,
                                          "page_name": exercise_name,
                                          "sub_exercise_list": art_evaluator_service.get_list_of_sub_exercises(exercise_name),
                                          "exercise_list": art_evaluator_service.get_list_of_exercises(),
                                          "bread_crumb_list": [(request.url_for("read_root"), "Home"),
                                                               (request.url_for("read_exercises"), "Exercises"),
                                                               (request.url_for("read_sub_exercises", exercise_name=exercise_name), "Categories")]
                                      })


@app.get("/exercises/{exercise_name}/{sub_exercise_name}", response_class=RedirectResponse)
async def generate_exercise(exercise_name: str, sub_exercise_name: str):
    exercise_id = art_evaluator_service.generate_exercises(exercise_name, sub_exercise_name)

    return f"/exercise/{exercise_id}"


@app.get("/exercise/{exercise_id}", response_class=HTMLResponse)
async def show_exercise(request: Request, exercise_id: int):
    dir_path = art_evaluator_service.get_filepath_of_dir(exercise_id)

    if dir_path is None:
        raise HTTPException(status_code=404, detail="This Exercise was not found")

    ex_info = art_evaluator_service.get_exercise_info(exercise_id)

    print(ex_info)
    return templates.TemplateResponse("exercise.html",
                                      {
                                          "request": request,
                                          "exercise_info": ex_info,
                                          "exercise_list": art_evaluator_service.get_list_of_exercises()
                                      })


@app.post("/exercise/{exercise_id}", response_class=FileResponse)
async def process_exercise_request(exercise_id: int, file_name: Annotated[str, Form()]):
    file_path = art_evaluator_service.get_file(exercise_id, file_name)

    if file_path is None:
        raise HTTPException(status_code=404, detail="Couldn't find file")

    return FileResponse(
        os.path.join(file_path),
        headers={'Content-Disposition': f'attachment; filename="{exercise_id}_{file_name}"'}
    )


@app.post("/exercise/{exercise_id}/submit", response_class=RedirectResponse)
async def process_exercise_submission(exercise_id: int, myfile: Annotated[UploadFile, File()]):
    if myfile.content_type != "image/png":
        raise HTTPException(400, "Please only upload png files")

    im_submission = Image.open(myfile.file)

    art_evaluator_service.store_submission(exercise_id, im_submission)
    await art_evaluator_service.generate_score(exercise_id)

    return RedirectResponse(f"/exercise/{exercise_id}", status_code=status.HTTP_303_SEE_OTHER)
