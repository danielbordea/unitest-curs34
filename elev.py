class Elev:
    #atribute, fields
    nume = ""
    prenume = ""
    cod_matricol = ""
    note = {}

    #construtor
    #tot timpul cand vreau sa fac un obiect caretrebuie sa aiba neparat ceva caracteristici le pun in constructor
    def __init__(self, nume, prenume, cod_matricol):
        self.nume = nume
        self.prenume = prenume
        self.cod_matricol = cod_matricol

    def descrie_elev(self):
        print(f"Ma numesc {self.nume} {self.prenume} si am cod matricol {self.cod_matricol}")

    def adauga_nota(self, materie,nota):
        self.note[materie] = nota


elev = Elev("Ion", "Barbu", "354565")
print(elev.nume)
print(elev.cod_matricol)
elev.descrie_elev()
print(elev.note)
elev.adauga_nota("matematica", 10)
elev.adauga_nota("romana", 5)
print(elev.note)

elev2 = Elev("Maria", "Muresan", "34545657")
elev2.adauga_nota("istori", 10)
elev2.adauga_nota("romana", 5)
print(elev2.note)
elev2.descrie_elev()

