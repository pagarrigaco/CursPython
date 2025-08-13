serie = "N-02"
client = {'nom':'Pau','edat':46,'genere':'home'}
peli = {'titol': 'Matrix', 'fitxa_tecnica':{'protagonista': 'Keannu Reeves',
                                            'director':'Lana i Lili Wachowski'}}

elements =[client,peli,'llibre']

for elem in elements:
    match elem:
        case{'nom':nom,'edat':edat,'genere':genere}:
            print('És un client')
            print(nom,edat,genere)
        case {'titol': titol, 'fitxa_tecnica': {'protagonista':prota,'director':dire}}:
            print('És una peli')
            print(titol, prota, dire)
        case _:
            print("No sé què és")


match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existeix aquesta marca")