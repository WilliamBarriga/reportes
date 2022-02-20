import json
from fastapi import FastAPI, BackgroundTasks, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response

from pydantic import BaseModel

from scraps.scrapPDET import scrapPDET
from scraps.scrapDepartamento import scrapDepartment
from utils.writedoc import write_document
from utils.utils import remove_file

from info import regions, departments
from dri_work.main import start_dri
from fDB.DRI_info import dri_subregiones, dri_departamentos, dri_regiones, dri_municipios, dri_types


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


@app.post(path='/api/scrap-department', response_class=FileResponse)
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


@app.post(path='/api/dri-report/{type_report}', response_class=FileResponse)
def dri_report(back: BackgroundTasks, type_report: str, name_place=Form(...), file: UploadFile = File(...)):

    if type_report == 'departamentos':
        type_report = 0

    elif type_report == 'municipios':
        type_report = 1

    elif type_report == 'subregiones':
        type_report = 2

    elif type_report == 'region':
        type_report = 3
    
    else:
        return Response(f'the info {type_report} is not defined', status_code=404)

    print(file.filename)
    file_Excel = file.file
    filer = start_dri(type_report, name_place, file_Excel)
    back.add_task(remove_file, filer)
    return filer


@app.get(path='/api/dri-info/{typeR}')
def get_dri_info(typeR: str):

    if typeR == 'departamentos':
        response = {'data': dri_departamentos}

    elif typeR == 'municipios':
        response = {'data': dri_municipios}

    elif typeR == 'subregiones':
        response = {'data': dri_subregiones}

    elif typeR == 'region':
        response = {'data': dri_regiones}

    else:
        return Response(f'the info {typeR} is not defined', status_code=404)

    return response
