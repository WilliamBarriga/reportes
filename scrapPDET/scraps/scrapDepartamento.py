import sys
import time
import logging
import pandas as pd

from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from scraps.utils import create_driver_scrap, remove_old_years, remove_chars



def scrapDepartment(region: int = 0):
    logging.basicConfig(
            format='%(asctime)s:%(levelname)s:%(message)s',
            level=logging.INFO,
            handlers=[
                logging.StreamHandler(sys.stdout)
            ])
    
    try:
        logging.info('starting process')
        info_doc = {}
        driver = create_driver_scrap()
        original_window = driver.current_window_handle
        logging.info('driver cargado')
        logging.info('seleccionando departamento')
        driver.implicitly_wait(5)
        department_select = driver.find_element(By.ID, 'departamento')
        department_drop = Select(department_select)
        department_drop.select_by_index(region)
        corte = driver.find_element(By.ID, 'cortes')
        corte.click()
        logging.info('click corte')
        m_corte = driver.find_element(By.XPATH, f'//*[@id="cortes"]/option[2]')
        m_corte.click()
        logging.info('click mes')
        
        driver.implicitly_wait(5)
        boton_consulta = driver.find_element(By.ID, 'btnCons')
        boton_consulta.click()
        logging.info('consultando')
        boletin = driver.find_element(By.XPATH, f'/html/body/div/div[3]/form/div/div/div[2]/div/div[2]/div[1]/div/div[1]/a')
        boletin.click()
        logging.info('click boletin')
        driver.implicitly_wait(5)
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        logging.info('cargando reporte')
        time.sleep(5)
        #sacando info reporte
        
        logging.info('-------------')
        logging.info('-------------')
        driver.implicitly_wait(15)
        regionPDET_reporte = driver.find_element(By.XPATH, f'//*[@id="portadaSec"]/div[2]/div[1]/div[1]/div/h2')
        logging.info(f'{regionPDET_reporte.text}')
        info_doc['regionPDET'] = regionPDET_reporte.text
        
        logging.info('-------------')
        num_victimas = driver.find_element(By.XPATH, f'//*[@id="Nacional"]/div/div[1]/div/div[1]/h1')
        logging.info(f'numero de victimas {num_victimas.text}')
        info_doc['num_victimas'] =  num_victimas.text
        
        porciento_poblacion = driver.find_element(By.XPATH, f'//*[@id="Nacional"]/div/div[1]/div/div[1]/h5')
        logging.info(f'{porciento_poblacion.text}')
        pp = porciento_poblacion.text[:6]
        info_doc['porcentaje_poblacion'] = pp
        
        logging.info('-------------')
        
        tabla = driver.find_element(By.XPATH, f'//*[@id="AtencHumanSub_284"]/tbody')
        table = tabla.text
        table = table.replace('.', '')
        df = remove_old_years(table)
        h_dinero_hogares_total = 0
        h_dinero_dinero_total = 0
        for year, info in df.iterrows():
            hogares = int(info[1])
            dinero = int(info[2].replace('$', ''))
            h_dinero_hogares_total += hogares
            h_dinero_dinero_total += dinero

        logging.info(f'dinero total gobierno: {h_dinero_dinero_total} millones')
        logging.info(f'hogares benediciados: {h_dinero_hogares_total}')
        info_doc['h_dinero_dinero'] = h_dinero_dinero_total
        info_doc['h_dinero_hogares'] = h_dinero_hogares_total
        
        logging.info('-------------')
        
        tabla = driver.find_element(By.XPATH, f'//*[@id="AtencHumanEsp_254"]/tbody')
        table = tabla.text
        table = table.replace('.', '')
        df = remove_old_years(table)
        h_especie_dinero_total = 0
        h_especie_hogares_total = 0
        for year, info in df.iterrows():
            hogares = remove_chars(info[1])
            dinero = remove_chars(info[2])
            h_especie_dinero_total += dinero
            h_especie_hogares_total += hogares
            
        logging.info(f'finero total gobierno especie {h_especie_dinero_total}')
        info_doc['h_especie_dinero'] = h_especie_dinero_total
        logging.info(f'hogares beneficiades en especie: {h_especie_hogares_total}')
        info_doc['h_especie_hogares'] = h_especie_hogares_total
        
        logging.info('-------------')
        
        tabla = driver.find_element(By.XPATH, f'//*[@id="AyuHumOtrosNoDespl_283"]/tbody')
        table = tabla.text
        table = table.replace('.', '')
        df = remove_old_years(table)
        h_hogares_diferente_desp_total = 0
        h_dinero_diferente_desp_total = 0
        
        for year, info in df.iterrows():
            hogares = remove_chars(info[1])
            dinero = remove_chars(info[2])
            h_hogares_diferente_desp_total += hogares
            h_dinero_diferente_desp_total += dinero
            
        
        logging.info(f'hogares total gobierno difere a desplazamiento: {h_hogares_diferente_desp_total}')
        info_doc['h_hogares_desp'] = h_hogares_diferente_desp_total
        logging.info(f'dinero total gobierno difere a desplazamiento: {h_dinero_diferente_desp_total} millones')
        info_doc['h_dinero_desp'] = h_dinero_diferente_desp_total
        
        
        logging.info('-------------')
        
        puntos_atencion = driver.find_element(By.XPATH, f'//*[@id="PunAtencion"]/tbody/tr/td/h5')
        cantidad_centros = driver.find_element(By.XPATH, f'//*[@id="CentrosRegionales_281"]/tfoot/tr/th[2]')
        solicitudes = driver.find_element(By.XPATH, f'//*[@id="TotalSol"]/tbody/tr/td/h5')
        personas_atendidas = driver.find_element(By.XPATH, f'//*[@id="PerAtendidas"]/tbody/tr/td/h5')
        logging.info(f'puntos {puntos_atencion.text}\n cantidad de centros {cantidad_centros.text}\n numero solicites {solicitudes.text}\n personas atendidas {personas_atendidas.text}')
        
        info_doc['puntos_atencion'] = puntos_atencion.text
        info_doc['cantidad_centro'] = cantidad_centros.text
        info_doc['solicitues'] = solicitudes.text
        info_doc['personas_atendidas'] = personas_atendidas.text
        
        logging.info('-------------')
        
        tabla = driver.find_element(By.XPATH, f'//*[@id="AtencHuman_269"]/tbody')
        table = tabla.text
        table = table.replace('.', '')
        df = remove_old_years(table)
        h_giros_hogares_total = 0
        h_giros_cantidad_total = 0
        h_giros_dinero_total = 0
        for year, info in df.iterrows():
            hogares = remove_chars(info[1])
            giros = remove_chars(info[2])
            dinero = remove_chars(info[3])
            h_giros_hogares_total += hogares
            h_giros_cantidad_total +=giros
            h_giros_dinero_total += dinero
        
        logging.info(f'giros totales {h_giros_cantidad_total}')
        info_doc['giros_totales'] = h_giros_cantidad_total
        logging.info(f'giros dinero {h_giros_dinero_total}')
        info_doc['giros_dinero'] = h_giros_dinero_total
        logging.info(f'giros hogares {h_giros_hogares_total}')
        info_doc['giros_hogares'] = h_giros_hogares_total
        
        logging.info('-------------')
        
        tabla = driver.find_element(By.XPATH, f'//*[@id="ProyComplAgro_258"]/tbody')
        table = tabla.text
        table = table.replace('.', '')
        df = remove_old_years(table)
        proyectos_agro_dinero_total = 0
        proyectos_agro_hogares_total = 0
        
        for year, info in df.iterrows():
            hogares = remove_chars(info[1])
            dinero = remove_chars(info[2])
            proyectos_agro_dinero_total += dinero
            proyectos_agro_hogares_total += hogares
        
        logging.info(f'dinero proy agro: {proyectos_agro_dinero_total}')
        info_doc['proyectos_agro_dinero'] = proyectos_agro_dinero_total
        logging.info(f'dinero proy agro: {proyectos_agro_hogares_total}')
        info_doc['proyectos_agro_hogares'] = proyectos_agro_hogares_total
        logging.info('-------------')

        tabla = driver.find_element(By.XPATH, f'//*[@id="Indemni_Disc_298"]/tbody')
        table = tabla.text
        table = table.replace('.', '')
        df = remove_old_years(table)
        indemnizaciones_ind_dinero_total = 0
        indemnizaciones_ind_numero_total = 0
        indemnizaciones_ind_personas_total = 0
        
        for year, info in df.iterrows():
            numero = remove_chars(info[1])
            personas = remove_chars(info[2])
            dinero = remove_chars(info[3])
            indemnizaciones_ind_dinero_total += dinero
            indemnizaciones_ind_numero_total += numero
            indemnizaciones_ind_personas_total += personas
        
        logging.info(f'dinero indemnizaciones: {indemnizaciones_ind_dinero_total}')
        info_doc['indemnizaciones_ind_dinero'] = indemnizaciones_ind_dinero_total
        logging.info(f'numero indemnizaciones: {indemnizaciones_ind_numero_total}')
        info_doc['indemnizaciones_ind_numero'] = indemnizaciones_ind_numero_total
        logging.info(f'personas indemnizaciones: {indemnizaciones_ind_personas_total}')
        info_doc['indemnizaciones_ind_personas'] = indemnizaciones_ind_personas_total
        
        logging.info('-------------')
        tabla = driver.find_element(By.XPATH, f'//*[@id="AtenPsicosocial_273"]/tbody')
        tabla = driver.find_element(By.XPATH, f'//*[@id="Indemni_Disc_298"]/tbody')
        table = tabla.text
        table = table.replace('.', '')
        
        df = remove_old_years(table)
        atencion_psicosocial_total = 0
        for year, info in df.iterrows():
            personas = remove_chars(info[1])
            atencion_psicosocial_total += personas
        logging.info(f'atencion psicosocial: {atencion_psicosocial_total}')
        info_doc['atencion_psicosocial'] = atencion_psicosocial_total
        logging.info('-------------')
        
        reparacion_colectiva_total = driver.find_element(By.XPATH, f'//*[@id="SujRepColec_271"]/tfoot/tr/th[5]')
        reparacion_colectiva_etnico = driver.find_element(By.XPATH, f'//*[@id="SujRepColec_271"]/tfoot/tr/th[2]')
        reparacion_colectiva_no_etnico = driver.find_element(By.XPATH, f'//*[@id="SujRepColec_271"]/tfoot/tr/th[3]')
        reparacion_colectiva_grp = driver.find_element(By.XPATH, f'//*[@id="SujRepColec_271"]/tfoot/tr/th[4]')
        
        logging.info(f'reparacion_colectiva_total: {reparacion_colectiva_total.text}')
        logging.info(f'reparacion_colectiva_etnico: {reparacion_colectiva_etnico.text}')
        logging.info(f'reparacion_colectiva_no_etnico: {reparacion_colectiva_no_etnico.text}')
        logging.info(f'reparacion_colectiva_grp: {reparacion_colectiva_grp.text}')
        
        info_doc['reparacion_colectiva_total'] = reparacion_colectiva_total.text.replace('.', '')
        info_doc['reparacion_colectiva_etnico'] = reparacion_colectiva_etnico.text.replace('.', '')
        info_doc['reparacion_colectiva_no_etnico'] = reparacion_colectiva_no_etnico.text.replace('.', '')
        info_doc['reparacion_colectiva_grp'] = reparacion_colectiva_grp.text.replace('.', '')
        
        logging.info('-------------')
        try:
            tabla = driver.find_element(By.XPATH, f'//*[@id="PlanRetorReub_266"]/tbody')
            tr_tabla = tabla.find_elements(By.TAG_NAME, 'tr')
            tr_tabla = len(tr_tabla)
            planes_reub_apro = driver.find_element(By.XPATH, f'//*[@id="PlanRetorReub_266"]/tbody/tr[{tr_tabla}]/td[2]')
            logging.info(f'planes_reub_apro: {planes_reub_apro.text}')
            info_doc['planes_reub_apro'] = planes_reub_apro.text.replace('.','.')
            try:
                planes_reub_for = driver.find_element(By.XPATH, f'//*[@id="PlanRetorReub_266"]/tbody/tr[{tr_tabla-2}]/td[2]')
                
                logging.info(f'planes_reub_for: {planes_reub_for.text}')
                info_doc['planes_reub_for'] = planes_reub_for.text.replace('.','.')
            
            except:
                logging.info('no hay reubicacion por formular')
                info_doc['planes_reub_for'] = 0
        except:
            logging.info('tabla sin informacion')
            info_doc['planes_reub_for'] = 0
            info_doc['planes_reub_apro'] = 0
        
        logging.info('-------------')
        driver.quit()
        logging.info(info_doc)
        logging.info('scrap terminado...')
        return info_doc

    
    except ValueError as e:
        logging.warning(f'a ocurrido el error: {e}')
        #logging.info(f'\n error en descarga de {regionPDET_reporte.text} reintentando')
        return None
    

