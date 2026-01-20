import json

file='numeros.json'

with open(file) as arxiu:
    numeros=json.load(arxiu)
print(numeros)