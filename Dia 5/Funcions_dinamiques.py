def comprovar_3_xifres(numero):
    return numero in range(100,1000) #comprova si el número està entre 100 i 999

resultat = comprovar_3_xifres(658)
print(resultat)

def comprovar_3_xifres_llista(llista):
    for n in llista:
        if n in range(100,1000): #atencio si en troba un surt del bucle
            return True
        else:
            pass

llistes = comprovar_3_xifres_llista([55,99,6,2])
print(llistes)

def comprovar_no3_xifres_llista(llista):
    existeix = False
    for n in llista:
        if n in range(100,1000): #busquem si no n'hi ha cap de 3 xifres
            existeix = True
            #return True MANERA MÉS OPTIMA
        else:
            pass
    #return False MANERA MÉS OPTIMA
    if (existeix):
        return True
    else:
        return False

llistes2 = comprovar_no3_xifres_llista([55,989,6,2])
print(llistes2)

def retornar_3_xifres_llista(llista):
    llista_de_3 = []
    for n in llista:
        if n in range(100,1000): #atencio si en troba un surt del bucle
            llista_de_3.append(n)
        else:
            pass
    return llista_de_3

llistes3 = retornar_3_xifres_llista([111,55,989,6,2])
print(llistes3)

#EXERCICIS

lista_numeros = [12, 3, 4, 5, 22, 67, 88]


def todos_positivos(llista):
    for n in llista:
        if n < 0:
            return False
        else:
            pass
    return True

lista_numeros = [10,10,10,101,-8]

def suma_menores(llista):
    suma = 0
    for n in llista:
        if (n<1000) and (n>0):
            suma += n
        else:
            pass
    return suma

print(suma_menores(lista_numeros))

lista_numeros = [2,2,4,3]

def cantidad_pares(llista):
    total = 0
    for n in llista:
        if n%2 == 0:
            total += 1
        else:
            pass
    return total

