'''
#EXCEPCIÓ ZERODIVISIONERROR
try:
    print(5/0)
except ZeroDivisionError:
    print("No puc dividir per 0")

#EXEMPLE TRY-EXCEPTION-ELSE
print("Dona'm dos números i en faig la divisió")
print("Apreta q quan vulguis sortir")

while True:
    primer_numero = input("\nIntrodueix el primer número: ")
    if primer_numero=='q':
        break
    segon_numero = input("Introdueix el segon número: ")
    if segon_numero == 'q':
        break
    try:
        resultat = int(primer_numero)/int(segon_numero)
    except ZeroDivisionError:
        print("\nNo puc dividir per 0")
    else:
        print(resultat)
'''

#EXCEPCIÓ FILE NOT FOUND

filename='text_files/lorem.txt'
'''
try:
    with open(filename,'r') as arxiu:
        content=arxiu.read()
except FileNotFoundError:
    print("Aquest arxiu no existeix")
'''
try:
    with open(filename, encoding='utf-8') as arxiu:
        contingut=arxiu.read()
except FileNotFoundError:
    print(f"L'arxiu {filename} no existeix")
else:
    paraules=contingut.split()
    num_paraules = len(paraules)
    print(f"L'arxiu {filename} conté un total de {num_paraules} paraules")
