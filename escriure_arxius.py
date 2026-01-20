filename='text_files/programacio.txt'
''' 
#MODE ESCRIPTURA D'UN ARXIU - SOBREESCRIU EL CONTINGUT
with open(filename,'w') as arxiu: #w -escriu, r -llegeix, a -les dues coses
    arxiu.write("Estic aprenent a programar\n")
    arxiu.write("De moment va prou bé.")
'''
#MODE A ON EL TEXT S'AFEGEIX AL FINAL DE L'ARXIU

with open(filename,'a') as arxiu:
    arxiu.write("I també m'agrada modelar en 3D\n")
