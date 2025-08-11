llista =['a','b','c']

for index,item in enumerate(llista): #utilitzem els enumerate per accedir als indexs
    print(index,item)

nou_tuple = list(enumerate(llista))
print(nou_tuple)

llista2 = list(enumerate("Python"))

print(llista2)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for index,nom in enumerate(lista_nombres):
    if nom[0]=='M':
        print(index)


