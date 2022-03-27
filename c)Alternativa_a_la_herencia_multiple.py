class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

    def añadir_ventanas(self, ventana):
        self.ventanas.append(ventana)

class Ventana:
    def __init__(self, pared, superficie, proteccion = False):
        self.pared = pared
        self.superficie = superficie
        self.pared.añadir_ventanas(self)

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        superficie = 0
        for i in self.paredes:
            for j in i.ventanas:
                superficie += j.superficie

        return superficie

class ParedCortina:
    def __init__(self, orientacion, superficie):
        self.orientacion = orientacion
        self.superficie = superficie

pared_norte = Pared('NORTE')
pared_oeste = Pared('OESTE')
pared_sur = Pared('SUR')
pared_este = Pared('ESTE')

ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)


casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_acristalada())



