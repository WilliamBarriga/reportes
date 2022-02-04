import pandas as pd
from pyxlsb import open_workbook

def read_logros():
    df = pd.read_excel('./Logros MADR_20_12_2021.xlsb', engine='pyxlsb')
    print(df.head(2))
    for col in df.columns.values:
        print(col)
    print('----------')
    for ind in df.index.values:
        print(ind)
        
    print('_____________')
    #df1 = df.xs('HUILA')
    #print(df1)
    #for val in df1.values:
    #    print(val)
    df.to_excel('./test.xlsx', engine='openpyxl')
    
    
if __name__ == '__main__':
    read_logros()