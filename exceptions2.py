from excepcions import filename


def contar(filename):
    try:
        with open(filename, encoding='utf-8') as arxiu:
            contingut = arxiu.read()
    except FileNotFoundError:
        #print(f"L'arxiu {filename} no existeix!")
        pass #NO FA RES QUAN FALLA, NO AVISA PERÒ SEGUEIX
    else:
        paraules=contingut.split()
        num_paraules = len(paraules)
        print(f"L'arxiu {filename} té un total de {num_paraules} paraules")

'''
#ARXIU ÚNIC
llibre='dracula.txt'
contar(llibre)
'''
#LLEGIR MULTIPLES ARXIUS
llibres=['dracula.txt','frankenstein.txt','alice.txt']
for llibre in llibres:
    contar(llibre)