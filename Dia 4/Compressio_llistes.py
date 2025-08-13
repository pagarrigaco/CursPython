paraula = 'python'

list =[]

llista2 = [lletra for lletra in paraula] #comprimim la llista
llista3 =[num for num in range(0,21,2)]
llista4 = [n if n*2 >10 else 'no' for n in range(0,21,2)] #podem posar condicions

for lletra in paraula:
    list.append(lletra)



print(list)
print(llista2)
print(llista3)
print(llista4)