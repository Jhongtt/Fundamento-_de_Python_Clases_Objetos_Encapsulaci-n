# Fundamento-_de_Python_Clases_Objetos_Encapsulaci-n

Cada objeto tiene sus propios valores para los atributos definidos en la clase. En este caso, ana y juan son dos objetos independientes, cada uno con sus propios valores de nombre y edad.

# Buenas prácticas para métodos #

- **Nombres descriptivos**: Usa verbos que describan claramente la acción que realiza el método.
- **Responsabilidad única**: Cada método debe hacer una sola cosa y hacerla bien.
- **Tamaño adecuado**: Mantén los métodos relativamente cortos y enfocados.
- **Validación de parámetros**: Verifica que los parámetros recibidos sean válidos.
- **Documentación**: Añade docstrings que expliquen qué hace el método, qué parámetros recibe y qué devuelve.
- **Consistencia**: Mantén un estilo consistente en todos los métodos de la clase.
- **Encapsulamiento**: Usa métodos para acceder y modificar atributos cuando sea necesario aplicar lógica adicional.

Los métodos son la parte activa de nuestras clases, definiendo el comportamiento de los objetos. Combinados con los atributos, nos permiten crear modelos completos y funcionales que representan entidades del mundo real en nuestro código.

**Aprendizajes de esta lección**

- Comprender el concepto de clases y objetos en programación orientada a objetos.
- Aprender a definir clases y crear objetos en Python.
- Entender el uso del método constructor **init** para inicializar objetos.
- Diferenciar entre atributos de instancia y de clase, y gestionar su acceso y modificación.
- Definir y utilizar métodos, incluyendo métodos especiales, estáticos y de clase, para modelar comportamientos de objetos.

# Programación Orientada a Objetos en Python

Resumen de los conceptos fundamentales de clases, objetos, atributos y métodos.

---

## ¿Qué es una Clase y un Objeto?

| Concepto | Analogía | En código |
|----------|----------|-----------|
| **Clase** | El plano de una casa | La plantilla/molde |
| **Objeto** | La casa ya construida | Una instancia concreta |

```python
class Perro:       # <-- esto es la CLASE (el molde)
    pass

fido = Perro()     # <-- esto es el OBJETO (el resultado)
rex  = Perro()     # otro objeto distinto, del mismo molde
```

---

## 🏗️ El Constructor `__init__`

Se ejecuta **automáticamente** al crear un objeto. Sirve para darle valores iniciales.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # guarda el nombre en el objeto
        self.edad   = edad     # guarda la edad en el objeto

ana  = Persona("Ana", 28)
juan = Persona("Juan", 35)

print(ana.nombre)   # Ana
print(juan.edad)    # 35
```

> **`self`** = referencia al objeto que se está creando. Siempre va primero, Python lo pasa solo.

---

## Atributos

Son las **características** del objeto (lo que "tiene" o "es").

### Atributos de instancia vs. de clase

```python
class Estudiante:
    universidad = "UNAL"          # atributo de CLASE  → compartido por todos

    def __init__(self, nombre):
        self.nombre = nombre      # atributo de INSTANCIA → único por objeto

e1 = Estudiante("María")
e2 = Estudiante("Carlos")

print(e1.universidad)   # UNAL  (compartido)
print(e1.nombre)        # María (solo de e1)
```

### Convenciones de visibilidad

| Prefijo | Ejemplo | Significado |
|---------|---------|-------------|
| Sin prefijo | `self.nombre` | Público, accesible desde cualquier lado |
| `_` un guión | `self._saldo` | "Protegido", no tocar desde fuera (convención) |
| `__` doble guión | `self.__pin` | "Privado", Python cambia el nombre internamente |

### Propiedades (`@property`)

Permiten validar o calcular valores al acceder a un atributo:

```python
class Temperatura:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura imposible")
        self._celsius = valor

t = Temperatura()
t.celsius = 25      # usa el setter (valida)
print(t.celsius)    # usa el getter
```

---

##  Métodos

Son los **comportamientos** del objeto (lo que "hace" o "puede hacer").

### Métodos de instancia

```python
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo  = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return f"Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad > self._saldo:
            return "Fondos insuficientes"
        self._saldo -= cantidad
        return f"Nuevo saldo: ${self._saldo}"

cuenta = CuentaBancaria("Ana", 1000)
print(cuenta.depositar(500))   # Nuevo saldo: $1500
print(cuenta.retirar(2000))    # Fondos insuficientes
```

### Métodos especiales 

Permiten que tus objetos usen operadores como `+`, `==`, `print()`, etc.

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):          # define qué muestra print()
        return f"({self.x}, {self.y})"

    def __add__(self, otro):    # define el operador +
        return Punto(self.x + otro.x, self.y + otro.y)

p1 = Punto(3, 4)
p2 = Punto(1, 2)
print(p1)        # (3, 4)
print(p1 + p2)   # (4, 6)
```

### Métodos estáticos y de clase

```python
class Utilidades:
    @staticmethod
    def es_par(n):          # no necesita self ni cls
        return n % 2 == 0

    @classmethod
    def info(cls):          # recibe la clase, no el objeto
        return f"Soy la clase {cls.__name__}"

print(Utilidades.es_par(4))   # True  — sin crear objeto
print(Utilidades.info())      # Soy la clase Utilidades
```

---

## Conceptos clave de POO

| Concepto | Qué significa |
|----------|---------------|
| **Abstracción** | Usar el objeto sin saber cómo funciona por dentro |
| **Encapsulamiento** | Agrupar datos + comportamiento en una sola unidad |
| **Reutilización** | Un mismo molde (clase) para muchos objetos |
| **Modularidad** | Cambiar el interior de una clase sin romper el resto |

---

## Buenas prácticas rápidas

- Nombrar clases en `PascalCase` → `MiClase`
- Nombrar métodos y atributos en `snake_case` → `mi_metodo`
- Inicializar **todos** los atributos en `__init__`
- Cada método debe hacer **una sola cosa**
- Usar `@property` cuando necesites validar un atributo
- Documentar con docstrings: `"""Esto hace..."""`


Taller Clases y Objetos en Python.

------------------------------------------------------------------------------------------------------------------------------------------------
##  Atributos privados**

En Python, la **encapsulación** permite controlar el acceso a los datos internos de una clase. Imagina una clase como una caja fuerte que contiene información valiosa: necesitamos mecanismos para proteger esa información y controlar cómo se accede a ella.

A diferencia de otros lenguajes como Java o C++, Python sigue una filosofía de "somos todos adultos aquí", lo que significa que no impone restricciones estrictas de acceso. Sin embargo, proporciona convenciones para indicar que ciertos atributos deben tratarse como **privados**.

### Convención de nombres para atributos privados**

En Python, la convención para marcar un atributo como privado es anteponer un guion bajo (`_`) al nombre del atributo:

En este ejemplo, `_titular` y `_saldo` son atributos que se consideran **privados por convención**. Esto significa que:

- Son detalles de implementación interna
- No deberían ser accedidos directamente desde fuera de la clase
- Podrían cambiar en futuras versiones de la clase

Sin embargo, esta convención es solo un **acuerdo entre programadores**. Técnicamente, aún es posible acceder a estos atributos desde fuera de la clase:

### Atributos "realmente" privados con doble guion bajo**

Para casos donde necesitamos un nivel mayor de protección, Python ofrece un mecanismo llamado **name mangling** (desfiguración de nombres) usando doble guion bajo (`__`):

Cuando usamos __pin, Python renombra internamente este atributo a _CuentaBancaria__pin. Esto hace más difícil (aunque no imposible) acceder al atributo desde fuera de la clase:

### **Cuándo usar atributos privados**

Los atributos privados son útiles en varias situaciones:

- **Proteger la integridad de los datos**: Cuando un atributo debe mantener ciertas restricciones (como un saldo que nunca debe ser negativo)
- **Ocultar detalles de implementación**: Para poder cambiar la implementación interna sin afectar el código que usa la clase
- **Evitar conflictos de nombres**: Especialmente en herencia, para evitar que las subclases sobrescriban accidentalmente atributos importantes

### **Ejemplo práctico: Validación de datos**

Un caso de uso común para atributos privados es cuando necesitamos validar los datos antes de asignarlos:

```python
class Producto:
```

### **Atributos privados vs. protegidos**

En la terminología de la programación orientada a objetos:

- **Atributos privados** (`__nombre`): Solo accesibles dentro de la propia clase
- **Atributos protegidos** (`_nombre`): Accesibles dentro de la clase y sus subclases

### **Buenas prácticas con atributos privados**

- **Usa un solo guion bajo** (`_nombre`) para la mayoría de los casos
- **Reserva el doble guion bajo** (`__nombre`) para evitar conflictos en la herencia o cuando realmente necesitas protección adicional
- **Documenta claramente** qué atributos son parte de la interfaz pública y cuáles son detalles de implementación
- **Proporciona métodos** para acceder y modificar atributos privados cuando sea necesario (veremos esto en la siguiente sección sobre getters y setters)

Los atributos privados son el primer paso para implementar una encapsulación efectiva en Python. Aunque el lenguaje no impone restricciones estrictas, seguir estas convenciones mejora significativamente la calidad y mantenibilidad del código.

## **Getters y setters**

Una vez que hemos definido atributos privados en nuestras clases, necesitamos una forma **controlada** de acceder y modificar estos datos. Aquí es donde entran en juego los getters y setters, que son métodos especiales diseñados para leer y escribir atributos privados de manera segura.

### **¿Por qué usar getters y setters?**

Los getters y setters nos permiten:

- **Validar datos** antes de asignarlos
- **Calcular valores** derivados bajo demanda
- **Controlar el acceso** a los atributos internos
- **Modificar la implementación interna** sin afectar el código cliente

En Python, los getters y setters se implementan como métodos normales, siguiendo una convención de nombres clara:


### **Uso de getters y setters**

Veamos cómo se utilizan estos métodos:


### **Ventajas de los getters y setters**

Los getters y setters ofrecen varias ventajas importantes:

- **Validación de datos**: Podemos verificar que los valores asignados cumplan con ciertas condiciones.
- **Encapsulación**: Ocultamos los detalles de implementación y exponemos solo lo necesario.
- **Flexibilidad**: Podemos cambiar la implementación interna sin afectar el código que usa la clase.
- **Depuración**: Facilitan la detección de problemas al centralizar el acceso a los datos.

### **Ejemplo práctico: Clase Producto**

Veamos un ejemplo más completo con una clase `Producto` que utiliza getters y setters para controlar el acceso a sus atributos:

### **Getters y setters en herencia**

Los getters y setters también son útiles en el contexto de la herencia, permitiendo a las subclases acceder y modificar atributos protegidos de manera controlada:

class Electrónico(Producto):
    def __init__(self, nombre, precio, stock, garantía_meses):
        super().__init__(nombre, precio, stock)
        self._garantía_meses = garantía_meses
        self._activado = False

    # Getters adicionales
    def get_garantía_meses(self):
        return self._garantía_meses

    def está_activado(self):
        return self._activado

    # Setters adicionales
    def set_garantía_meses(self, meses):
        if not isinstance(meses, int) or meses < 0:
            raise ValueError("Los meses de garantía deben ser un entero positivo")
        self._garantía_meses = meses

    def activar(self):
        self._activado = True

    def desactivar(self):
        self._activado = False

    # Sobrescribir el setter de precio para añadir lógica adicional
    def set_precio(self, nuevo_precio):
        # Llamamos al setter de la clase padre
        super().set_precio(nuevo_precio)
        # Lógica adicional específica para productos electrónicos
        if nuevo_precio > 1000:
            # Productos caros tienen garantía extendida automáticamente
            self._garantía_meses = max(self._garantía_meses, 24)

    ### **Consideraciones sobre el uso de getters y setters**

Aunque los getters y setters son útiles, es importante usarlos con criterio:

- **No crees getters y setters para todo**: Solo para atributos que necesiten validación o lógica especial.
- **Mantén la simplicidad**: Si un atributo no necesita validación ni procesamiento, considera si realmente necesita getters y setters.
- **Sé consistente**: Si decides usar getters y setters, úsalos de manera consistente en toda la clase.

### **Getters y setters vs. acceso directo**

En Python, a diferencia de lenguajes como Java, no es obligatorio usar getters y setters para todos los atributos. Para atributos simples que no requieren validación, a veces es aceptable permitir el acceso directo:


# Taller Clases y Objetos en Python.

Crear una clase Libro con atributos y métodos para gestionar información básica

Crea una clase llamada `Libro` que represente un libro en una biblioteca. La clase debe tener los siguientes atributos:

- `titulo`: el título del libro
- `autor`: el autor del libro
- `paginas`: el número total de páginas
- `disponible`: un booleano que indica si el libro está disponible para préstamo (inicialmente `True`)

La clase debe tener los siguientes métodos:

1. Un constructor (`__init__`) que inicialice los atributos mencionados
2. Un método `prestar()` que cambie el estado de disponibilidad a `False` y devuelva un mensaje indicando que el libro ha sido prestado. Si el libro ya está prestado, debe devolver un mensaje indicando que no está disponible.
3. Un método `devolver()` que cambie el estado de disponibilidad a `True` y devuelva un mensaje indicando que el libro ha sido devuelto. Si el libro ya está disponible, debe devolver un mensaje indicando que el libro ya estaba en la biblioteca.
4. Un método `informacion()` que devuelva una cadena con toda la información del libro, incluyendo su estado de disponibilidad.

Prueba tu clase creando al menos dos objetos libro diferentes y llamando a todos sus métodos.