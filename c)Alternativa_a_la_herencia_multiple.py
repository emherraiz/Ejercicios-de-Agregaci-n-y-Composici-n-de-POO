class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

    def añadir_ventanas(self, ventana):
        self.ventanas.append(ventana)

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        self.pared.añadir_ventanas(self)

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        superficie_total = 0
        for pared in self.paredes:
            print(f'La pared: {pared} contiene las ventanas')
            for ventana in pared.ventanas:
                print(f'{ventana} ------ {ventana.superficie}')
                superficie_total += ventana.superficie

        return superficie_total



## ENUNCIADO 1
# Instanciación de las paredes
pared_norte = Pared('NORTE')
pared_oeste = Pared('OESTE')
pared_sur = Pared('SUR')
pared_este = Pared('ESTE')

# Instanciación de las ventanas
ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)

# Instanciación de la casa con 4 paredes
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_acristalada())


## ENUNCIADO 2
class ParedCortina(Pared):
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.orientacion = orientacion
        Ventana(self, superficie)


casa.paredes[2] = ParedCortina('SUR', 10)
print(casa.superficie_acristalada())

## ENUNCIADO 3

class Ventana_regulada:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        self.pared.añadir_ventanas(self)

        if proteccion is None:
            raise Exception('Necesitas proteccion')
        else:
            self.proteccion = proteccion

# ventana_norte = Ventana_regulada(pared_norte, 0.5)

# ventana_norte = Ventana_regulada(pared_norte, 0.5, None)

ventana_norte = Ventana_regulada(pared_norte, 0.5, 'Persiana')
print(casa.superficie_acristalada())






