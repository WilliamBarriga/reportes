import logging
import os
import sys
import pandas as pd
import json
from .write_doc import write_doc_dri
from fDB.DRI_info import dri_types, dri_subregiones

cwd = os.getcwd()
base_file = f'{cwd}/dri_work/Logros MADR_20_12_2021.xlsb'


def read_form_tierras(info_doc, type_report, name_place, file) -> dict:
    info_doc = {}
    index_columns = [1, 2, 13, 14]
    index_col = index_columns[type_report]

    df = pd.read_excel(base_file, engine='pyxlsb',
                       sheet_name="Formalización de tierras ANT", skiprows=6, index_col=index_col)

    # subregion PDET: int / otros: str
    df = df.xs(name_place)

    if type(df) == pd.core.frame.DataFrame:
        info_doc['Titulos_Expedidos'] = df.loc[:, 'Títulos formalizados'].sum()
        info_doc['Hectareas_for'] = round(
            df.loc[:, 'Área formalizada en hectáreas'].sum())
        info_doc['Familias_for'] = df.loc[:, 'Familias beneficiadas'].sum()
        info_doc['Mujeres_for'] = df.loc[:, 'Mujeres beneficiadas'].sum()
        info_doc['Hectareas_ingresadas'] = round(
            df.loc[:, 'Hectareas incorporadas en el Fondo de Tierras'].sum())

    elif type(df) == pd.core.series.Series:
        info_doc['Titulos_Expedidos'] = df['Títulos formalizados']
        info_doc['Hectareas_for'] = round(df['Área formalizada en hectáreas'])
        info_doc['Familias_for'] = df['Familias beneficiadas']
        info_doc['Mujeres_for'] = df['Mujeres beneficiadas']
        info_doc['Hectareas_ingresadas'] = df['Hectareas incorporadas en el Fondo de Tierras']

    return info_doc


def read_URT(info_doc, type_report, name_place, file) -> dict:
    index_columns = [1, 2, 12, 13]
    index_col = index_columns[type_report]
    df = pd.read_excel(base_file, engine='pyxlsb',
                       sheet_name="URT", skiprows=6, index_col=index_col)

    df = df.xs(name_place)

    if type(df) == pd.core.frame.DataFrame:
        info_doc['URT_personas'] = df.loc[:,'No. de Personas beneficiadas en sentencia ruta individual'].sum()
        info_doc['URT_mujeres'] = df.loc[:,'Número de mujeres beneficiadas en sentencia de ruta individual'].sum()
        info_doc['URT_predios'] = round(
            df.loc[:, 'No. de predios identificados en sentencia con orden de restitución y/o compensación-ruta individual'].sum())
        info_doc['URT_hectareas'] = round(
            df.loc[:, 'No. de hectáreas con orden de restitución y/o compensación en sentencia ruta individual'].sum())
        info_doc['URT_fam_proy'] = df.loc[:,
                                          'Familias beneficiadas con proyectos productivos'].sum()
        info_doc['URT_inv_proy'] = round(
            df.loc[:, 'Inversión familias beneficiadas con proyectos productivos'].sum())
        info_doc['URT_fam_subsidio'] = df.loc[:,
                                              'Familias con atención de subsidio de vivienda'].sum()

    elif type(df) == pd.core.series.Series:
        info_doc['URT_personas'] = df['No. de Personas beneficiadas en sentencia ruta individual'].sum()
        info_doc['URT_mujeres'] = df['Número de mujeres beneficiadas en sentencia de ruta individual'].sum()
        info_doc['URT_predios'] = round(
            df['No. de predios identificados en sentencia con orden de restitución y/o compensación-ruta individual'].sum())
        info_doc['URT_hectareas'] = round(
            df['No. de hectáreas con orden de restitución y/o compensación en sentencia ruta individual'].sum())
        info_doc['URT_fam_proy'] = df['Familias beneficiadas con proyectos productivos'].sum()
        info_doc['URT_inv_proy'] = round(
            df['Inversión familias beneficiadas con proyectos productivos'].sum())
        info_doc['URT_fam_subsidio'] = df['Familias con atención de subsidio de vivienda'].sum()

    return info_doc


def read_vivienda(info_doc, type_report, name_place, file) -> dict:
    index_columns = [1, 2, 11, 12]
    index_col = index_columns[type_report]
    df = pd.read_excel(base_file, engine='pyxlsb',
                       sheet_name='Vivienda', skiprows=6, index_col=index_col)

    df = df.xs(name_place)

    if type(df) == pd.core.frame.DataFrame:

        info_doc['Vivienda_Total'] = df.loc[:,
                                            'Total soluciones de vivienda (otorgamientos periodo de gobierno)'].sum()
        info_doc['Vivienda_nueva'] = df.loc[:,
                                            'Viviendas nuevas (otorgamientos periodo de gobierno)'].sum()
        info_doc['Vivienda_mejorada'] = df.loc[:,'Viviendas mejoradas (otorgamientos periodo de gobierno)'].sum()
        info_doc['Vivienda_subsidio_total'] = round(
            df.loc[:, 'Valor total total de subsidios entregados ($)'].sum())
        info_doc['Vivienda_subsidio_nueva'] = round(
            df.loc[:, 'Valor subsidios vivienda nuevas ($)'].sum())
        info_doc['Vivienda_subsidio_mejorada'] = round(
            df.loc[:, 'Valor subsidios mejoramiento ($)'].sum())
    elif type(df) == pd.core.series.Series:

        info_doc['Vivienda_Total'] = df['Total soluciones de vivienda (otorgamientos periodo de gobierno)'].sum(
        )
        info_doc['Vivienda_nueva'] = df['Viviendas nuevas (otorgamientos periodo de gobierno)'].sum(
        )
        info_doc['Vivienda_mejorada'] = df['Viviendas mejoradas (otorgamientos periodo de gobierno)'].sum(
        )
        info_doc['Vivienda_subsidio_total'] = round(
            df['Valor total total de subsidios entregados ($)'].sum())
        info_doc['Vivienda_subsidio_nueva'] = round(
            df['Valor subsidios vivienda nuevas ($)'].sum())
        info_doc['Vivienda_subsidio_mejorada'] = round(
            df['Valor subsidios mejoramiento ($)'].sum())

    return info_doc


def read_alianzas_productivas(info_doc, type_report, name_place, file) -> dict:
    index_columns = [1, 2, 18, 19]
    index_col = index_columns[type_report]
    df = pd.read_excel(base_file, engine='pyxlsb',
                       sheet_name='Alianzas productivas', skiprows=6, index_col=index_col)

    df = df.xs(name_place)

    if type(df) == pd.core.frame.DataFrame:

        info_doc['alipro_nproyectos'] = df.loc[:,'No. de proyectos (Alianzas)'].sum()
        info_doc['alipro_nbeneficiarios'] = df.loc[:,'No. de beneficiarios'].sum()
        info_doc['alipro_npresupuesto'] = round(
            df.loc[:, 'Valor de ejecución presupuestal ($)'].sum())
    elif type(df) == pd.core.series.Series:
        info_doc['alipro_nproyectos'] = df['No. de proyectos (Alianzas)'].sum()
        info_doc['alipro_nbeneficiarios'] = df['No. de beneficiarios'].sum()
        info_doc['alipro_npresupuesto'] = round(
            df['Valor de ejecución presupuestal ($)'].sum())

    return info_doc


def read_coseche_y_venda(info_doc, type_report, name_place, file) -> dict:
    index_columns = [1, 2, 6, 7]
    index_col = index_columns[type_report]
    df = pd.read_excel(base_file, engine='pyxlsb',
                       sheet_name='Coseche y venda a la fija', skiprows=6, index_col=index_col)

    df = df.xs(name_place)
    if type(df) == pd.core.frame.DataFrame:
        info_doc['coseche_venda_productores'] = df.loc[:,'Productores con acuerdos comerciales'].sum()
        info_doc['coseche_venda_inversion'] = round(
            df.loc[:, 'Valor estimado acuerdos comerciales ($)'].sum())
    elif type(df) == pd.core.series.Series:
        info_doc['coseche_venda_productores'] = df['Productores con acuerdos comerciales'].sum()
        info_doc['coseche_venda_inversion'] = round(
            df['Valor estimado acuerdos comerciales ($)'].sum())

    return info_doc


def read_financiamiento(info_doc, type_report, name_place, file) -> dict:
    index_columns = [1, 2, 93, 94]
    index_col = index_columns[type_report]
    df = pd.read_excel(base_file, engine='pyxlsb',
                       sheet_name='Financiamiento', skiprows=6, index_col=index_col)

    df = df.xs(name_place)

    if type(df) == pd.core.frame.DataFrame:
        info_doc['Finagro_creditos'] = df.loc[:,'Número de operaciones de Crédito de Fomento Agropecuario'].sum()
        info_doc['Finagro_dinero'] = round(
            df.loc[:, 'Valor del Crédito de Fomento Agropecuario ($)'].sum())
        info_doc['LEC_operaciones'] = df.loc[:,'Número de operaciones - LEC'].sum()
        info_doc['LEC_creditos'] = round(
            df.loc[:, 'Valor crédito ($) - LEC'].sum())
        info_doc['LEC_subsidiones'] = round(
            df.loc[:, 'Valor subsidio ($) - LEC'].sum())
    elif type(df) == pd.core.series.Series:
        info_doc['Finagro_creditos'] = df['Número de operaciones de Crédito de Fomento Agropecuario'].sum()
        info_doc['Finagro_dinero'] = round(
            df['Valor del Crédito de Fomento Agropecuario ($)'].sum())
        info_doc['LEC_operaciones'] = df['Número de operaciones - LEC'].sum()
        info_doc['LEC_creditos'] = round(df['Valor crédito ($) - LEC'].sum())
        info_doc['LEC_subsidiones'] = round(
            df['Valor subsidio ($) - LEC'].sum())

    return info_doc


def read_campo(info_doc, type_report, name_place, file) -> dict:
    index_columns = [1, 2, 14, 15]
    index_col = index_columns[type_report]
    df = pd.read_excel(base_file, engine='pyxlsb',
                       sheet_name='Construyendo capacidades', skiprows=6, index_col=index_col)

    df = df.xs(name_place)

    if type(df) == pd.core.frame.DataFrame:
        info_doc['campo_proyectos'] = df.loc[:, 'Proyectos productivos'].sum()
        info_doc['campo_familias'] = df.loc[:,'Familias beneficiarias de generación de capacidades "El Campo Emprende"'].sum()
        info_doc['campo_dinero'] = round(
            df.loc[:, 'Recursos de generación de capacidades "El Campo Emprende"  ($)'].sum())
    elif type(df) == pd.core.series.Series:
        info_doc['campo_proyectos'] = df['Proyectos productivos'].sum()
        info_doc['campo_familias'] = df['Familias beneficiarias de generación de capacidades "El Campo Emprende"'].sum()
        info_doc['campo_dinero'] = round(
            df['Recursos de generación de capacidades "El Campo Emprende"  ($)'].sum())

    return info_doc


def fix_nums(json_nums) -> dict:
    for k, v in json_nums.items():
        try:
            v = '{:,}'.format(v).replace(',', '.')
            json_nums[k] = v

        except:
            logging.info(f'error converting number: {v} key: {k}')

    return json_nums


def start_dri(type_report, name_place, file_Excel):
    logging.basicConfig(
        format='%(asctime)s:%(levelname)s:%(message)s',
        level=logging.INFO,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ])
    typeR = dri_types[type_report]
    name = name_place
    info_doc = {}

    if type_report == 2:
        logging.info('Reporte Subregion')
        name_place = dri_subregiones.index(name_place)
        name_place += 1

    #index_columns: ['Departamento', 'Municipio', 'Subregión PDET', 'Región']
    info_doc = read_form_tierras(info_doc, type_report, name_place, file_Excel)
    info_doc = read_URT(info_doc, type_report, name_place, file_Excel)
    info_doc = read_vivienda(info_doc, type_report, name_place, file_Excel)
    info_doc = read_alianzas_productivas(
        info_doc, type_report, name_place, file_Excel)
    info_doc = read_coseche_y_venda(
        info_doc, type_report, name_place, file_Excel)
    info_doc = read_financiamiento(
        info_doc, type_report, name_place, file_Excel)
    info_doc = read_campo(info_doc, type_report, name_place, file_Excel)
    logging.info('**************')
    info_doc = fix_nums(info_doc)

    info_doc['Report_type'] = typeR
    info_doc['Name_Place'] = name

    logging.info(info_doc)

    file = write_doc_dri(info_doc)
    return file
