#Ejemplo conceptual en este caso un libro
class Libro:
    def __init__(self, titulo, autor, paginas): # Aquí definiremos atributos como título, autor, páginas
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    # Y métodos como abrir(), leer(), cerrar()
    pass

abrir = Libro("Libro abiero")

# Creamos objetos (instancias) de la clase Libro
libro_python = Libro()  # Un libro específico sobre Python
novela_fantasia = Libro()  # Una novela de fantasía específica


#el pass se usa para cuando hay algo vacio ya que esto daria un error al estar vacio por eso se una el pass para que no de error y el sistema 
#lo detecte

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creamos un objeto Persona
ana = Persona("Ana García", 28)

# Python internamente hace algo equivalente a:
# Persona.__init__(ana, "Ana García", 28)

# Creamos dos objetos Persona
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

# Accedemos a sus atributos
print(ana.nombre)  # Imprime: Ana García
print(juan.edad)   # Imprime: 35

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Creamos productos con y sin especificar el stock
laptop = Producto("Laptop XPS", 1200)  # stock será 0
teclado = Producto("Teclado mecánico", 80, 15)  # stock será 15

print(laptop.stock)  # Imprime: 0
print(teclado.stock)  # Imprime: 15


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto  # Calculamos y almacenamos el área
        self.perimetro = 2 * (ancho + alto)  # Calculamos y almacenamos el perímetro

# Creamos un rectángulo
rect = Rectangulo(5, 3)
print(rect.area)      # Imprime: 15
print(rect.perimetro) # Imprime: 16


class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular

        # Validamos que el saldo inicial no sea negativo
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.saldo = saldo_inicial

# Esto funcionará
cuenta_ana = Cuenta("Ana García", 1000)

# Esto lanzará un ValueError
try:
    cuenta_problematica = Cuenta("Juan López", -500)
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: El saldo inicial no puede ser negativo

   #class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0

# Creamos algunos libros
libro1 = Libro("Python Crash Course", "Eric Matthes", 544, "9781593279288")
libro2 = Libro("Clean Code", "Robert C. Martin", 464, "9780132350884", False)

# Verificamos si están disponibles
print(f"{libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}")
print(f"{libro2.titulo} está {'disponible' if libro2.disponible else 'prestado'}")


class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        """Constructor alternativo que crea una Fecha desde un texto con formato DD-MM-AAAA"""
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        """Constructor alternativo que crea una Fecha con la fecha actual"""
        import datetime
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)

# Diferentes formas de crear objetos Fecha
fecha1 = Fecha(15, 3, 2023)  # Constructor normal
fecha2 = Fecha.desde_texto("25-12-2023")  # Constructor alternativo
fecha3 = Fecha.hoy()  # Constructor alternativo que usa la fecha actual

print(f"{fecha1.dia}/{fecha1.mes}/{fecha1.año}")  # Imprime: 15/3/2023
print(f"{fecha2.dia}/{fecha2.mes}/{fecha2.año}")  # Imprime: 25/12/2023

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
        self.activo = True    # Atributo de instancia con valor predeterminado

# Creamos dos estudiantes
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

# Cada estudiante tiene sus propios valores para los atributos
print(estudiante1.nombre)  # Imprime: María
print(estudiante2.nombre)  # Imprime: Carlos

class Estudiante:
    # Atributo de clase
    universidad = "Universidad Autónoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

# Creamos dos estudiantes
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

# Ambos comparten el mismo atributo de clase
print(estudiante1.universidad)  # Imprime: Universidad Autónoma
print(estudiante2.universidad)  # Imprime: Universidad Autónoma
print(Estudiante.universidad)   # También podemos acceder desde la clase

# Si modificamos el atributo de clase, afecta a todas las instancias
Estudiante.universidad = "Universidad Complutense"
print(estudiante1.universidad)  # Imprime: Universidad Complutense
print(estudiante2.universidad)  # Imprime: Universidad 

class Producto:
    impuesto = 0.21  # Atributo de clase

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Creamos un producto
laptop = Producto("Laptop", 1000)

# Accedemos a sus atributos
print(laptop.nombre)    # Atributo de instancia
print(laptop.precio)    # Atributo de instancia
print(laptop.impuesto)  # Atributo de clase (accedido desde la instancia)
print(Producto.impuesto)  # Atributo de clase (accedido desde la clase)





class Estudiante:
    universidad = "Universidad Autónoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

print(estudiante1.universidad)  # Universidad Autónoma
print(estudiante2.universidad)  # Universidad Autónoma
print(Estudiante.universidad)

Estudiante.universidad = "Universidad Complutense"
print(estudiante1.universidad)  # Universidad Complutense
print(estudiante2.universidad)  # Universidad Complutense

class Producto:
    impuesto = 0.21

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

laptop = Producto("Laptop", 1000)
print(laptop.nombre)
print(laptop.precio)
print(laptop.impuesto)
print(Producto.impuesto)


class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0

mi_coche = Coche("Toyota", "Corolla", "Azul")
mi_coche.color = "Rojo"
mi_coche.kilometraje = 1500
print(f"Nuevo color: {mi_coche.color}")
print(f"Kilometraje: {mi_coche.kilometraje}")


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

juan = Persona("Juan")
juan.edad = 30
juan.profesion = "Ingeniero"
print(f"{juan.nombre} tiene {juan.edad} años y es {juan.profesion}")


# hasattr / getattr / setattr / delattr
p = Persona("Laura")
p.edad = 29
print(hasattr(p, "nombre"))   # True
print(hasattr(p, "apellido")) # False
print(getattr(p, "nombre"))
print(getattr(p, "apellido", "No especificado"))
setattr(p, "apellido", "García")
print(p.apellido)
delattr(p, "apellido")

class CuentaBancaria:
    tasa_interes = 0.03

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin

    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

cuenta = CuentaBancaria("Ana López", 1000, "1234")
print(cuenta.titular)
print(cuenta._saldo)
print(cuenta._CuentaBancaria__pin)  # name mangling


class Temperatura:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9

temp = Temperatura()
temp.celsius = 25
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")
temp.fahrenheit = 68
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto

    @property
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

rect = Rectangulo(5, 3)
print(f"Área: {rect.area}")
print(f"Perímetro: {rect.perimetro}")
rect.ancho = 7
print(f"Nueva área: {rect.area}")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"
        return f"{self.marca} {self.modelo} ya estaba apagado"

    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} está apagado"
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad máxima alcanzada: {self.velocidad} km/h"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0:
            return "El coche ya está detenido"
        nueva_velocidad = self.velocidad - decremento
        if nueva_velocidad < 0:
            self.velocidad = 0
            return "Coche detenido"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.encender())
print(mi_coche.acelerar(50))
print(mi_coche.acelerar(30))
print(mi_coche.frenar(20))
print(mi_coche.frenar(60))


class Calculadora:
    def sumar(self, a, b): return a + b
    def restar(self, a, b): return a - b
    def multiplicar(self, a, b): return a * b
    def dividir(self, a, b):
        if b == 0: return "Error: División por cero"
        return a / b
    def calcular_estadisticas(self, numeros):
        if not numeros:
            return {"suma": 0, "promedio": 0, "minimo": None, "maximo": None}
        return {
            "suma": sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "minimo": min(numeros),
            "maximo": max(numeros)
        }

calc = Calculadora()
print(calc.sumar(5, 3))
print(calc.dividir(10, 0))
stats = calc.calcular_estadisticas([4, 7, 2, 9, 5])
print(stats)


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."

persona = Persona("Juan", "Pérez", 25)
print(persona.presentarse())

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        if not isinstance(otro, Punto):
            return False
        return self.x == otro.x and self.y == otro.y

    def __len__(self):
        return abs(self.x) + abs(self.y)

p1 = Punto(3, 4)
p2 = Punto(1, 2)
print(p1)           # (3, 4)
print(repr(p1))     # Punto(3, 4)
print(p1 + p2)      # (4, 6)
print(p1 == p2)     # False
print(p1 == Punto(3, 4))  # True
print(len(p1))      # 7


class Ejemplo:
    """Clase de ejemplo para mostrar atributos especiales"""
    def __init__(self, valor):
        self.valor = valor

obj = Ejemplo(42)
print(obj.__class__)
print(Ejemplo.__name__)
print(Ejemplo.__doc__)
print(obj.__dict__)

class MathUtils:
    @staticmethod
    def es_primo(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n == 0 or n == 1: return 1
        return n * MathUtils.factorial(n - 1)

print(MathUtils.es_primo(17))   # True
print(MathUtils.es_primo(20))   # False
print(MathUtils.factorial(5))   # 120


class Empleado:
    num_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1

    @classmethod
    def desde_salario_anual(cls, nombre, salario_anual):
        return cls(nombre, salario_anual / 12)

    @classmethod
    def obtener_num_empleados(cls):
        return cls.num_empleados

emp1 = Empleado("Ana", 3000)
emp2 = Empleado.desde_salario_anual("Carlos", 48000)
print(f"Empleados creados: {Empleado.obtener_num_empleados()}")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"
        self._saldo += cantidad
        return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva"
        if cantidad > self._saldo:
            return "Fondos insuficientes"
        self._saldo -= cantidad
        return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

cuenta = CuentaBancaria("Ana López", 1000)
print(cuenta.consultar_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.retirar(2000))

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
        self.abierto = False

    def abrir(self):
        if self.abierto:
            return f"{self.titulo} ya está abierto"
        self.abierto = True
        return f"{self.titulo} ha sido abierto"

    def cerrar(self):
        if not self.abierto:
            return f"{self.titulo} ya está cerrado"
        self.abierto = False
        return f"{self.titulo} ha sido cerrado"

    def leer(self, num_paginas):
        if not self.abierto:
            return f"No puedes leer: {self.titulo} está cerrado"
        if self.pagina_actual >= self.paginas:
            return f"Ya has terminado de leer {self.titulo}"
        paginas_restantes = self.paginas - self.pagina_actual
        paginas_a_leer = min(num_paginas, paginas_restantes)
        self.pagina_actual += paginas_a_leer
        if self.pagina_actual >= self.paginas:
            return f"Has leído {paginas_a_leer} páginas y has terminado {self.titulo}"
        return f"Has leído {paginas_a_leer} páginas. Estás en la página {self.pagina_actual} de {self.paginas}"

    def reiniciar_lectura(self):
        self.pagina_actual = 0
        return f"Has reiniciado la lectura de {self.titulo}"

    def __str__(self):
        estado = "abierto" if self.abierto else "cerrado"
        progreso = f"{self.pagina_actual}/{self.paginas} páginas"
        return f"{self.titulo} por {self.autor} - {progreso} - {estado}"

libro = Libro("El Quijote", "Miguel de Cervantes", 863)
print(libro.leer(50))
print(libro.abrir())
print(libro.leer(50))
print(libro.leer(100))
print(libro.cerrar())
print(libro.abrir())
print(libro.leer(713))
print(libro.reiniciar_lectura())
print(libro)

