import docx
from docx.shared import Pt 
from docx.enum.style import WD_STYLE_TYPE





def write_document(info: dict):
    regionPDET= info['regionPDET']
    num_victimas= info['num_victimas']
    porcentaje_poblacion= info['porcentaje_poblacion']
    h_dinero_dinero= info['h_dinero_dinero']
    h_dinero_hogares= info['h_dinero_hogares']
    h_especie_dinero= info['h_especie_dinero']
    h_especie_hogares= info['h_especie_hogares']
    h_dinero_desp= info['h_dinero_desp']
    h_hogares_desp= info['h_hogares_desp']
    puntos_atencion= info['puntos_atencion']
    cantidad_centro= info['cantidad_centro']
    solicitues= info['solicitues']
    personas_atendidas= info['personas_atendidas']
    giros_totales= info['giros_totales']
    giros_dinero= info['giros_dinero']
    giros_hogares= info['giros_hogares']
    proyectos_agro_dinero= info['proyectos_agro_dinero']
    proyectos_agro_hogares= info['proyectos_agro_hogares']
    indemnizaciones_ind_dinero= info['indemnizaciones_ind_dinero']
    indemnizaciones_ind_numero= info['indemnizaciones_ind_numero']
    indemnizaciones_ind_personas= info['indemnizaciones_ind_personas']
    atencion_psicosocial= info['atencion_psicosocial']
    reparacion_colectiva_total= info['reparacion_colectiva_total']
    reparacion_colectiva_etnico= info['reparacion_colectiva_etnico']
    reparacion_colectiva_no_etnico= info['reparacion_colectiva_no_etnico']
    reparacion_colectiva_grp= info['reparacion_colectiva_grp']
    planes_reub_apro= info['planes_reub_apro']
    planes_reub_for= info['planes_reub_for']
    
    doc = docx.Document('./Víctimas.docx')
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial Narrow'
    font.size = Pt(12)

    paragraphs = doc.paragraphs
    
    registro_u_victimas = paragraphs[2]
    registro_u_victimas.text = registro_u_victimas.text.replace('num_victimas', f'{num_victimas}')
    registro_u_victimas.text = registro_u_victimas.text.replace('porcentaje_poblacion', f'{porcentaje_poblacion}')
    registro_u_victimas.style = style
    
    ayuda_h_dinero = paragraphs[5]
    ayuda_h_dinero.text = ayuda_h_dinero.text.replace('h_dinero_dinero', f'{h_dinero_dinero}')
    ayuda_h_dinero.text = ayuda_h_dinero.text.replace('h_dinero_hogares', f'{h_dinero_hogares}')
    
    ayuda_h_especie = paragraphs[8]
    ayuda_h_especie.text = ayuda_h_especie.text.replace('h_especie_dinero', f'{h_especie_dinero}')
    ayuda_h_especie.text = ayuda_h_especie.text.replace('h_especie_hogares', f'{h_especie_hogares}')
    
    ayuda_h_desp = paragraphs[11]
    ayuda_h_desp.text = ayuda_h_desp.text.replace('h_dinero_desp', f'{h_dinero_desp}')
    ayuda_h_desp.text = ayuda_h_desp.text.replace('h_hogares_desp', f'{h_hogares_desp}')
    
    atencion = paragraphs[14]
    atencion.text = atencion.text.replace('puntos_atencion', f'{puntos_atencion}')
    atencion.text = atencion.text.replace('cantidad_centro', f'{cantidad_centro}')
    atencion.text = atencion.text.replace('solicitues', f'{solicitues}')
    atencion.text = atencion.text.replace('personas_atendidas', f'{personas_atendidas}')
    
    giros_h = paragraphs[17]
    giros_h.text = giros_h.text.replace('giros_totales', f'{giros_totales}')
    giros_h.text = giros_h.text.replace('giros_dinero', f'{giros_dinero}')
    giros_h.text = giros_h.text.replace('giros_hogares', f'{giros_hogares}')
    
    proyectos_agro = paragraphs[20]
    proyectos_agro.text = proyectos_agro.text.replace('proyectos_agro_dinero', f'{proyectos_agro_dinero}')
    proyectos_agro.text = proyectos_agro.text.replace('proyectos_agro_hogares', f'{proyectos_agro_hogares}')
    
    indemnizaciones_ind = paragraphs[23]
    indemnizaciones_ind.text = indemnizaciones_ind.text.replace('indemnizaciones_ind_dinero', f'{indemnizaciones_ind_dinero}')
    indemnizaciones_ind.text = indemnizaciones_ind.text.replace('indemnizaciones_ind_numero', f'{indemnizaciones_ind_numero}')
    indemnizaciones_ind.text = indemnizaciones_ind.text.replace('indemnizaciones_ind_personas', f'{indemnizaciones_ind_personas}')
    
    psicosocial = paragraphs[26]
    psicosocial.text = psicosocial.text.replace('atencion_psicosocial', f'{atencion_psicosocial}')
    
    reparacion_colectiva = paragraphs[28]
    reparacion_colectiva.text = reparacion_colectiva.text.replace('reparacion_colectiva_total', f'{reparacion_colectiva_total}')
    reparacion_colectiva.text = reparacion_colectiva.text.replace('reparacion_colectiva_etnico', f'{reparacion_colectiva_etnico}')
    reparacion_colectiva.text = reparacion_colectiva.text.replace('reparacion_colectiva_no_etnico', f'{reparacion_colectiva_no_etnico}')
    reparacion_colectiva.text = reparacion_colectiva.text.replace('reparacion_colectiva_grp', f'{reparacion_colectiva_grp}')
    
    retornos = paragraphs[30]
    retornos.text = retornos.text.replace('planes_reub_apro', f'{planes_reub_apro}')
    retornos.text = retornos.text.replace('planes_reub_for', f'{planes_reub_for}')
    
    dir_save= f'files/{regionPDET}.docx'
    doc.save(dir_save)
    
    return dir_save