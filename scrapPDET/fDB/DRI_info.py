import json

dri_info = {
    "Subregión PDET": {
        1: "Alto Patia - Nore del Cauca",
        2: "Pacifico y Frontera Nariñense",
        3: "Sierra Nevada - Perija",
        4: "Uraba Antioqueño",
        5: "Cuenca del Caguan y Pie de Montre Caqueteño",
        6: "Montes de Maria",
        7: "Arauca",
        8: "Bajo Cauca y Nordeste Atioqueño",
        9: "Catatumbo",
        10: "Putumayo",
        11: "Sur de Bolivar",
        12: "Sur de Cordoba",
        13: "Sur de Tolima",
        14: "Choco",
        15: "Macarena - Guaviare",
        16: "Medio Pacifico"
    },
}

dri_types = {
    0: 'Departamento',
    1: 'Municipio',
    2: 'Subregión PDET',
    3: 'Región',
}

dri_departamentos = json.load(open('./fDB/DRI_Departamentos.json'))

dri_regiones = json.load(open('./fDB/DRI_Regiones.json'))

dri_municipios = json.load(open('./fDB/DRI_Municipios.json'))
