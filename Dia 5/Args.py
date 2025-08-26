def suma(*args):
    total = 0
    for num in args:
        total += num
    return total

print(suma(5,6,25,100))

#EXERCICI 1
def suma_cuadrados(*args):
    total = 0
    for num in args:
        total += (num**2)
    return total

#EXERCICI 2
def suma_absolutos(*args):
    total = 0
    for num in args:
        total += abs(num)
    return total

#EXERCICI 3
def numeros_persona(nombre, *args):
    suma_numeros = 0
    text = ''
    for num in args:
        suma_numeros += num
    text = (f"{nombre}, la suma de tus números es {suma_numeros}")
    return text
