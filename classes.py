#EXEMPLES DE CLASSES
class Gos:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def seu(self):
        print(f"{self.nom} s'ha assegut")
    def fer_volta(self):
        print(f"{self.nom} ha fet la croqueta")
class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any
        self.quilometratge = 0

    def nom_comercial(self):
        print(f"{self.marca} {self.model} {self.any}")
    def quilometres(self):
        print(f"El model {self.marca} {self.model} {self.any} porta un total de {self.quilometratge}")
    def modificar_quilometres(self,km):
        self.quilometratge += km
        print(f"El model {self.marca} {self.model} {self.any} porta un total de {self.quilometratge}")
#CLASSE DERIVADA describim atributs com a classes per facilitar la legibilitat
class Bateria:
    def __init__(self):
        self.bateria =100
    def nivell_bateria(self):
        print(f"Està al {self.bateria} % de càrrega")
    def descarregar_bateria(self,bateria):
        self.bateria -= bateria
        print(f"Està al {self.bateria} % de càrrega")
    def carregar_bateria(self,bateria):
        self.bateria += bateria
        print(f"Està al {self.bateria} % de càrrega")
#HERENCIA utilitzem una classe ja existent per crear-ne una de nova
class CotxeElectric(Cotxe):
    def __init__(self,marca,model,any):
        super().__init__(marca,model,any)
        self.bateria = Bateria()



el_meu_gos = Gos('Bobby',5)
print(f"El meu gos es diu {el_meu_gos.nom} i té {el_meu_gos.edat} anys")
el_meu_gos.seu()
el_meu_gos.fer_volta()
print("\n")

cotxe = Cotxe ('Ford','Fiesta',1995)
cotxe.nom_comercial()
cotxe.quilometres()
cotxe.modificar_quilometres(25)
cotxe.modificar_quilometres(25)
print("\n")
tesla = CotxeElectric('Tesla','Model S',2025)
tesla.nom_comercial()
tesla.bateria.nivell_bateria()
tesla.bateria.descarregar_bateria(20)
tesla.bateria.carregar_bateria(5)
