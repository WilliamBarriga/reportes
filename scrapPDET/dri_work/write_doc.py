import os
import docx
from uuid import uuid4

cwd = os.getcwd()

def write_doc_dri(json_info: dict):
    
    doc = docx.Document(f'{cwd}/base_docx/DRI.docx')
    
    paras = doc.paragraphs
    
    #i=0
    #for para in paras:
    #    print('-'*25)
    #    print(f'{i}.\n {para.text}')
    #    i += 1
    
    para = paras[0]
    para.text = para.text.replace('#ZonaR', json_info["Name_Place"])
    para.text = para.text.replace('#TipoR', json_info["Report_type"])
    
    para = paras[4]
    para.text = para.text.replace('#Personas', json_info["URT_personas"])
    para.text = para.text.replace('#Mujeres', json_info["URT_mujeres"])
    
    para = paras[6]
    para.text = para.text.replace('#Hectareas', json_info["URT_hectareas"])
    
    para = paras[8]
    para.text = para.text.replace('#Predios', json_info["URT_predios"])
    
    para = paras[10]
    para.text = para.text.replace('#Familias', json_info["URT_fam_proy"])
    para.text = para.text.replace('#Dinero', json_info["URT_inv_proy"])
    
    para = paras[12]
    para.text = para.text.replace('#Familias', json_info["URT_fam_subsidio"])
    
    para = paras[17]
    para.text = para.text.replace('#Hectareas', json_info["Hectareas_ingresadas"])
    
    para = paras[19]
    para.text = para.text.replace('#Hectareas', json_info["Hectareas_for"])
    para.text = para.text.replace('#titulos', json_info["Titulos_Expedidos"])
    para.text = para.text.replace('#Familias', json_info["Familias_for"])
    para.text = para.text.replace('#Mujeres', json_info["Mujeres_for"])
    
    para = paras[21]
    para.text = para.text.replace('#Personas', json_info["alipro_nbeneficiarios"])
    para.text = para.text.replace('#Proyectos', json_info["alipro_nproyectos"])
    para.text = para.text.replace('#Dinero', json_info["alipro_npresupuesto"])
    
    para = paras[23]
    para.text = para.text.replace('#Familias', json_info["campo_familias"])
    para.text = para.text.replace('#Proyectos', json_info["campo_proyectos"])
    para.text = para.text.replace('#Dinero', json_info["campo_dinero"])
    
    para = paras[26]
    para.text = para.text.replace('#Creditos', json_info["Finagro_creditos"])
    para.text = para.text.replace('#Dinero', json_info["Finagro_dinero"])
    
    para = paras[28]
    para.text = para.text.replace('#Creditos', json_info["LEC_operaciones"])
    para.text = para.text.replace('#Dinero', json_info["LEC_creditos"])
    para.text = para.text.replace('#Subsidio', json_info["LEC_subsidiones"])
    
    para = paras[30]
    para.text = para.text.replace('#Productores', json_info["coseche_venda_productores"])
    para.text = para.text.replace('#Dinero', json_info["coseche_venda_inversion"])
    
    para = paras[34]
    para.text = para.text.replace('#TViviendas', json_info["Vivienda_Total"])
    para.text = para.text.replace('#ViviendasMejora', json_info["Vivienda_mejorada"])
    para.text = para.text.replace('#ViviendasNuevas', json_info["Vivienda_nueva"])
    
    para = paras[35]
    para.text = para.text.replace('#TotalDinero', json_info["Vivienda_subsidio_total"])
    
    para = paras[36]
    para.text = para.text.replace('#DineroNuevo', json_info["Vivienda_subsidio_nueva"])
    para.text = para.text.replace('#DineroMejora', json_info["Vivienda_subsidio_mejorada"])
    
    path_file = f'{cwd}/DRI {json_info["Report_type"]} {json_info["Name_Place"]}_{uuid4()}.docx'
    doc.save(path_file)
    return path_file