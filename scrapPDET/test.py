import json

a = json.load(open('./fDB/DRI_subregiones.json'))

b = a.index('Alto Patia - Norte del Cauca')
print(b)
print(b + 1)
