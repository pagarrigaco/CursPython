filename='text_files/programacio.txt'

with open(filename,'w') as arxiu: #w -escriu, r -llegeix, a -les dues coses
    arxiu.write("Estic aprenent a programar\n")
    arxiu.write("De moment va prou bé.")