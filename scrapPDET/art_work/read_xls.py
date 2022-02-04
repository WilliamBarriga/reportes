import pandas as pd



def read_proyects(file, region_name='NACIONAL'):
    proyectos_pdet = {}
    ocad_paz = {}
    df = pd.read_excel(file, index_col=[2, 1], sheet_name='base_automatización')
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.xs(region_name)
    df1 = df.xs('OCAD PAZ')
    ocad_paz['total_proyectos'] = df1['total proyectos']
    #for val in df1.values:
    #    print(val)


if __name__ == '__main__':
    file = './BASE_ART.xlsx'
    region_name = 'ALTO PATÍA - NORTE DEL CAUCA'
    read_proyects(file, region_name)