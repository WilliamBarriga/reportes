import pandas as pd

from io import StringIO
from selenium import webdriver



def create_driver_scrap():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    
    driver.get('http://fichaestrategica.unidadvictimas.gov.co/BoletinPDET/IndexPDET')
    driver.maximize_window()
    
    return driver


def remove_old_years(table):
    table = table.replace(' ', ',')
    df = pd.read_csv(StringIO(table), sep=',', header=None, index_col=0)
    df = df[~df.index.duplicated(keep='first')]
    for row, info in df.iterrows():
        if type(row) == str:
            try:
                row2 = int(row)
                if row2 < 2018:
                    df = df.drop(row)
            except Exception:
                df = df.drop(row)
        elif row < 2018:
            df = df.drop(row)
    return df

def remove_chars(word):
    word = str(word)
    word = word.replace('.','')
    word = word.replace('$', '')
    word = int(word)
    return word