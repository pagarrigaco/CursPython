llista = ['a','b','c']
llista2 =['d','e','f']
resultat = len(llista)
valor = llista[1]
llista3 = llista+llista2

desordenats = ['g','u','a','c','z','m']

llista3[0] ='z' #les llistes son mutables
llista3.append('g') #es poden agregar elements
element_eliminat = llista3.pop(0)
#llista3.pop(0) #sense paràmetres elimina l'últim

print(type(llista))
print(resultat)
print(valor)
print(llista+llista2)
print(llista3)
desordenats.sort() #no ho podem guardar en un valor
print(desordenats)
desordenats.reverse() #ordena a l'inversa
print(desordenats)