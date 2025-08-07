llista = ['a', 'b', 'c', 'd']
llista2 =['Pau','Montse', 'Júlia', 'Àlex', 'Pere', 'Maria']
numeros =[1,2,3,4,5]
valor = 0
dic = {'clau1':'a', 'clau2':'b', 'clau3':'c'}

for element in llista:
    numero_lletra = llista.index(element) + 1
    print(f"Lletra {numero_lletra}: " + element)

for noms in llista2:
    if noms.startswith('M'):
        print(noms)
print(f"Aquí la variable valor val: {valor}")
for numero in numeros:
    valor = valor + numero

print(f"Però aquí la variable valor val: {valor}")

for item in dic: #imprimeix les claus
    print(item)
for item in dic.items(): #imprimeix claus i valors
    print(item)
for item in dic.values(): #imprimeix els valors
    print(item)