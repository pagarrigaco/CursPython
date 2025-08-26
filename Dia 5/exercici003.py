def zeros_repetits(*args):
    repetit = False
    aux = 0
    for valor in args:
        if valor == 0:
           aux +=1
        else:
            aux = 0
        if aux == 2:
            repetit = True
        if repetit:
            break;
    return repetit

print(zeros_repetits(5,6,1,0,0,9,3,5))