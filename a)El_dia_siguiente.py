class Edificio:
    def __init__(self, name):
        self.name = name
        self.ciudad = None
        self.empresa = None

    def obtener_edificio(self):
        return self.name

    def __del__(self):
        print(f'El edificio {self.name} es destruido')

class Empleado:
    def __init__(self, name):
        self.name = name
        self.empresa = None
    def __del__(self):
        print(f'El empleado {self.name} es despedido, la empresa quebró por la falta de instalaciones')


class Ciudad:

    def __init__(self, nombre):
        self.edificios = []
        self.nombre = nombre

    def anadir_edificios(self, lista):
        for i in range(len(lista)):
            self.edificios.append(Edificio(lista[i]))

    def obtener_edificios(self):
        return self.edificios

    def __del__(self):
        print(f'La ciudad {self.nombre} fue destruida por una catastrofe')

class Empresa():

    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
        self.empleados = []
        self.edificios = []

    def añadir_empleados(self, lista):
        for i in range(len(lista)):
            self.empleados.append(Empleado(lista[i]))

    def añadir_edificios(self, lista):
        for i in range(len(lista)):
            x = lista[i].obtener_edificio()
            opcion = input(f'¿Es el edificio {x} parte de {self.nombre_empresa}?\n')
            if opcion.lower == 'SI':
                self.edificios.append(lista[i])

    def obtener_edificios(self):
        return self.edificios

    def __del__(self):
        print(f'La empresa {self.nombre_empresa} quiebra por falta de instalaciones')

nueva_york = Ciudad('Nueva York')
LA = Ciudad('Los Angeles')
nueva_york.anadir_edificios(['A', 'B'])
LA.anadir_edificios(['C'])
print(nueva_york.obtener_edificios())
YooHoo = Empresa('YooHoo')
YooHoo.añadir_empleados(['Martin', 'Salim', 'Xing'])
YooHoo.añadir_edificios(nueva_york.obtener_edificios())
YooHoo.añadir_edificios(LA.obtener_edificios())
del nueva_york




