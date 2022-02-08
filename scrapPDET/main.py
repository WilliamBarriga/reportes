from fastapi import staticfiles

from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse, Response

from pydantic import BaseModel

from scraps.scrapPDET import scrapPDET
from scraps.scrapDepartamento import scrapDepartment
from utils.writedoc import write_document
from utils.utils import remove_file

from info import regions, departments
from dri_work.main import start_dri
import json


class Scrap(BaseModel):
    region: int


class Dri(BaseModel):
    type_report: int
    name_place: str or int


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(path='/api/scrap-region', response_class=FileResponse)
def scrap_pdet(data: Scrap, back: BackgroundTasks):
    region = data.region
    info = None
    while info == None:
        info = scrapPDET(region)
    file = write_document(info)
    back.add_task(remove_file, file)
    return file


@app.post(path='/api/scrap-department',response_class=FileResponse)
def scrap_department(data: Scrap, back: BackgroundTasks):
    department = data.region
    info = None
    while info == None:
        info = scrapDepartment(department)
    file = write_document(info)
    back.add_task(remove_file, file)
    return file


@app.get(path='/api/get/{data}')
def get_regions(data: str):
    if data == 'regions':
        return {'data': regions}
    elif data == 'departments':
        return {'data': departments}
    else:
        return Response(f'the info {data} is not defined', status_code=404)
    

@app.post(path='/api/dri-report', response_class=FileResponse)
def dri_report(data: Dri, back: BackgroundTasks):
    type_report = data.type_report
    name_place = data.name_place
    file = start_dri(type_report, name_place)
    back.add_task(remove_file, file)
    return file