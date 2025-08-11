for num in range(1,6):
    print(num)

for num2 in range(1,20,2): #ensenya els números de 2 en 2
    print(num2)

llista = list(range(1,101)) #creem una llista del 1 al 100
print(llista)

suma_cuadrados = 0

for num in range(1,16):
    potencia = int(num**0.5)
    print(f"La potencia de {num} és {potencia}")
    suma_cuadrados = suma_cuadrados + potencia
print(suma_cuadrados)