import pandas as pd
from pyxlsb import open_workbook

def _regions_name(name_place):
    regions = {
        10: 'Putumayo'
    }

    return regions[name_place]

def read_form_tierras(type_report, name_place) -> dict:
    info_doc = {}
    #index_columns: ['Departamento', 'Municipio', 'Subregión PDET', 'Región']
    index_columns= [1, 2, 13, 14]
    index_col = index_columns[type_report]
    
    df = pd.read_excel('./Logros MADR_20_12_2021.xlsb', engine='pyxlsb', sheet_name="Formalización de tierras ANT", skiprows=6, index_col=index_col)
    
    #subregion PDET: int / otros: str 
    df = df.xs(name_place)
    if type(name_place) == int:
        name_place = _regions_name(name_place)
    
    info_doc['Name_place'] = name_place
    info_doc['Titulos_Expedidos'] = df.loc[:, 'Títulos formalizados'].sum()
    info_doc['Hectareas_for'] = round(df.loc[:, 'Área formalizada en hectáreas'].sum())
    info_doc['Familias_for'] = df.loc[:, 'Familias beneficiadas'].sum()
    info_doc['Mujeres_for'] = df.loc[:, 'Mujeres beneficiadas'].sum()
    info_doc['Hectareas_ingresadas'] = round(df.loc[:, 'Hectareas incorporadas en el Fondo de Tierras'].sum())
    
    return info_doc


def read_URT(info_doc, type_report, name_place) -> dict:
    index_columns= [1, 2, 12, 13]
    index_col = index_columns[type_report]
    df = pd.read_excel('./Logros MADR_20_12_2021.xlsb', engine='pyxlsb', sheet_name="URT", skiprows=6, index_col=index_col)
    
    
    print('----------')
    print(df.head(2))
    for col in df.columns.values:
        print(col)
    print('----------')
    
    
    df = df.xs(name_place)
    
    info_doc['URT_personas'] = df.loc[:, 'No. de Personas beneficiadas en sentencia ruta individual'].sum()
    info_doc['URT_mujeres'] = df.loc[:, 'Número de mujeres beneficiadas en sentencia de ruta individual'].sum()
    info_doc['URT_predios'] = round(df.loc[:, 'No. de predios identificados en sentencia con orden de restitución y/o compensación-ruta individual'].sum())
    info_doc['URT_hectareas'] = round(df.loc[:, 'No. de hectáreas con orden de restitución y/o compensación en sentencia ruta individual'].sum())
    info_doc['URT_fam_proy'] = df.loc[:, 'Familias beneficiadas con proyectos productivos'].sum()
    info_doc['URT_inv_proy'] = round(df.loc[:, 'Inversión familias beneficiadas con proyectos productivos'].sum())
    info_doc['URT_fam_subsidio'] = df.loc[:, 'Familias con atención de subsidio de vivienda'].sum()
    
    return info_doc



if __name__ == '__main__':
    ############################## Remove at finish
    #print('----------')
    #print(df.head(2))
    #for col in df.columns.values:
    #    print(col)
    #print('----------')
    ################################
    params = (2, 10)
    info_doc = read_form_tierras(*params)
    info_doc = read_URT(info_doc, *params)
    info_doc = 
    
    print('**************')
    print(info_doc)
    