'''
#EXERCICI 1--------------------------------
with open('text_files/digits.txt') as arxiu:
    contents = arxiu.read()
print(contents.rstrip()) #rstrip() elimina últim salt de linia

#EXERCICI 2--------------------------------
filename= 'pi_digits.txt'
with open(filename) as arxiu:
    lines = arxiu.readlines()

for line in lines:
    print(line.rstrip())

#EXERCICI 3 -------------------------------
filename='pi_digits.txt'

with open(filename) as arxiu:
    lines=arxiu.readlines()
pi_string=''

for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))
'''
#EXERCICI 4------------------------------

filename='pi_digits.txt'

with open(filename) as arxiu:
    lines=arxiu.readlines()
pi_string=''

for line in lines:
    pi_string+=line.rstrip()

print(pi_string.strip())
aniversari=input("Entra el teu aniversari (mmddyy): ")
if aniversari in pi_string:
    print("El teu aniversari surt al número PI!")
else:
    print("El teu aniversari no apareix dins el número PI")