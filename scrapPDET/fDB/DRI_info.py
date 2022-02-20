import json

dri_types = {
    0: 'Departamento',
    1: 'Municipio',
    2: 'Subregión PDET',
    3: 'Región',
}

dri_subregiones = json.load(open('./fDB/DRI_subregiones.json'))

dri_departamentos = json.load(open('./fDB/DRI_Departamentos.json'))

dri_regiones = json.load(open('./fDB/DRI_Regiones.json'))

dri_municipios = json.load(open('./fDB/DRI_Municipios.json'))
