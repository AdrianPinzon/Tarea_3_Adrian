class Empleado:
    def __init__(self, rol, nombre, cedula, balance=0):
        self.rol = rol
        self.nombre = nombre
        self.cedula = cedula
        self.balance = balance
    
    def retirar_dinero(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print("Retiro exitoso. Nuevo balance: $" + str(self.balance))
        else:
            print("No tiene suficiente saldo para realizar el retiro.")
    
    def pagar_salario(self, cantidad):
        self.balance += cantidad
        print("Pago de salario exitoso. Nuevo balance: $" + str(self.balance))

class Nomina:
    def __init__(self, presupuesto_inicial):
        self.empleados = []
        self.presupuesto = presupuesto_inicial
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print("El empleado " + empleado.nombre + " ha sido agregado exitosamente a la nómina.")
    
    def mostrar_empleados(self):
        print("Lista de empleados:")
        for empleado in self.empleados:
            print("- " + empleado.nombre + " (" + empleado.rol + ")")
    
    def pagar_nomina(self):
        total_pagos = 0
        for empleado in self.empleados:
            if empleado.rol == "Programador Junior":
                cantidad_a_pagar = 1000
            elif empleado.rol == "Programador Senior":
                cantidad_a_pagar = 2000
            elif empleado.rol == "Manager":
                cantidad_a_pagar = 3000
            else:
                cantidad_a_pagar = 0
            
            if cantidad_a_pagar <= self.presupuesto:
                empleado.pagar_salario(cantidad_a_pagar)
                total_pagos += cantidad_a_pagar
                self.presupuesto -= cantidad_a_pagar
            else:
                print("No hay suficiente presupuesto para pagar el salario de " + empleado.nombre + ".")
        
        print("Se han pagado un total de $" + str(total_pagos) + " en salarios.")
    
    def agregar_presupuesto(self, cantidad):
        self.presupuesto += cantidad
        print("Se han agregado $" + str(cantidad) + " al presupuesto de la nómina. Presupuesto actual: $" + str(self.presupuesto))

def menu():
    print("Bienvenido a la nómina.")
    print("1. Agregar empleado")
    print("2. Mostrar lista de empleados")
    print("3. Pagar nómina")
    print("4. Agregar presupuesto")
    print("5. Salir")

nomina = Nomina(10000)

while True:
    menu()
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del empleado: ")
        rol = input("Ingrese el rol del empleado: ")
        cedula = input("Ingrese la cedula: ")
        empleado = Empleado(nombre, rol, cedula)
        nomina.agregar_empleado(empleado)
    
    elif opcion == "2":
        nomina.mostrar_empleados()
    
    elif opcion == "3":
        nomina.pagar_nomina()
    
    elif opcion == "4":
        cantidad = int(input("Ingrese la cantidad a agregar al presupuesto: "))
        nomina.agregar_presupuesto(cantidad)
    
    elif opcion == "5":
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")

print("Gracias por usar la nómina.")    

