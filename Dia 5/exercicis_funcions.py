from random import randint
from random import choice

#EXERCICI 1
def lanzar_dados():
    valor1 = randint(1, 7)
    valor2 = randint(1, 7)
    return valor1, valor2

def evaluar_jugada(dau1, dau2):
    suma_dados = dau1 + dau2
    resultat = ''
    if suma_dados <= 6:
        resultat = (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        resultat = (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        resultat = (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

    return resultat

dau1, dau2 = lanzar_dados()
text = evaluar_jugada(dau1, dau2)
print(text)

#EXERCICI 2
lista_numeros =[1,2,15,7,2]
print(lista_numeros)
def reducir_lista(llista):
    llista = list(set(llista))
    llista.sort()
    llista.pop()
    return llista
def promedio(llista):
    promig = sum(llista)/len(llista)
    return promig
llista = reducir_lista(lista_numeros)
promedio(llista)

#EXERCICI 3
lista_numeros=[1,2,3,4,5,6,7,8,9]
def lanzar_moneda():
    moneda = ['Cara','Cruz']
    tirada = choice(moneda)
    return tirada
def probar_suerte(moneda,lista_numeros):
    if moneda == 'Cara':
        print('La lista se autodestruirá')
        lista_numeros.clear()
    else:
        print('La lista fue salvada')
    return lista_numeros

moneda = lanzar_moneda()
probar_suerte(moneda,lista_numeros)



