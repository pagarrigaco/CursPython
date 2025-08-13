from random import * #importa tots els métodes de la llibreria random

aleatori = randint(1,50)
aleatori2 = round(uniform(1,5),1) #decimals i els arrodonim per evitar molts decimals
aleatori3 = random() #escull un decimal entre 0 i 1
colors = ['blau', 'vermell', 'verd','groc']
aleatori4 = choice(colors) #escull dins d'una llista
numeros = list(range(5,50,5)) #llista de cada cinc números entre 5 i 50



print(aleatori)
print(aleatori2)
print(aleatori3)
print(aleatori4)
print(f"Llista de números ordenada {numeros}")
shuffle(numeros)
print(numeros)