class Empleado:
    def __del__(self):
        print(f'El empleado {self.name} a sido despedido de la empresa devido a la desapariciónde la misma')
    def __init__(self, name):
        self.name = name

class Edificio:
    def __del__(self):
        print(f'El edificio {self.name} es destruido')
    def __init__(self, name):
        self.name = name
        self.ciudad = None

class Ciudad:
    def __del__(self):
        print(f'{self.name} fue desturida devido a la catastrofe')
    def __init__(self, edificios_ciudad):
        self.edificios = [Edificio(name) for name in edificios_ciudad]

class Empresa:
    def __del__(self):
        print(f'La empresa {self.name} a dejado de operar devido a que ya no le queda ninguna sede')
    def __init__(self, edificios_empresa, empleados):
        self.edificios = [Edificio(name) for name in edificios_empresa]
        self.trabajador = [Empleado(name) for name in empleados]

empresaA = Empresa(['A', 'B', 'C'], ['Martin', 'Salim', 'Xing'])
