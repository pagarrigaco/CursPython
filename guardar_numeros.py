import json

numeros=[1,3,5,7,9]

file='numeros.json'

with open(file,'w') as arxiu:
    json.dump(numeros, arxiu)