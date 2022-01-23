from io import StringIO
import pandas as pd


x = '''
2013 25 $21
2013 25 $21
2014 48 $32
2014 48 $32
2015 83 $54
2015 83 $54
2016 106 $76
2016 106 $76
2017 82 $90
2017 82 $90
2018 159 $202
2018 159 $202
2019 162 $148
2020 123 $125
2021 96 $96
'''

x = x.replace(' ', ',')

df = pd.read_csv(StringIO(x), header=None, index_col=0)
df = df.drop_duplicates()
for row in df.index:
    if row < 2018:
        df = df.drop(row)

totalhogares = 0
totaldinero = 0
for year, info in df.iterrows():
    hogares = int(info[1])
    dinero = int(info[2].replace('$', ''))
    print(dinero)
    totalhogares += hogares
    totaldinero += dinero

print('+++++++++++')
print(totalhogares)
print(totaldinero)