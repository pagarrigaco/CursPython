def es_primer(valor):

    total = 0
    iteracio = 2
    if valor <2:
        return 0

    while iteracio <= valor:
        for n in range(2,iteracio):
            if iteracio % n == 0:
                iteracio +=1
                break;
        else:
            iteracio+=1
            total += 1
    return total

numero = input("Introdueix el valor: ")
numeros_primers = es_primer(int(numero))
print (f"El total de números primers entre 0 i {numero} és de: {numeros_primers}")
