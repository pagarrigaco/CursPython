def retornar_diferents(valor1, valor2, valor3):
    suma = valor1+valor2+valor3
    valor_retornar = 0
    llista = [valor1,valor2,valor3]

    if suma > 15:
        valor_retornar = max(llista)
    elif suma <10:
        valor_retornar = min(llista)
    elif (suma>=10) and (suma <=15):
        valor_retornar = suma - (max(llista)+min(llista))
    return valor_retornar

print(retornar_diferents(5,6,1))