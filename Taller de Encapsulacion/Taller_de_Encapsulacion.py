class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self.saldo = saldo          # usa el setter para validar desde el inicio

    # --- Propiedad titular: solo lectura ---
    @property
    def titular(self):
        return self._titular
    # no hay @titular.setter → no se puede modificar

    # --- Propiedad saldo: lectura y escritura con validación ---
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    # --- Métodos ---
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


# --- Pruebas ---
cuenta = CuentaBancaria("Ana García", 1000)

print(cuenta.titular)   # Ana García
print(cuenta.saldo)     # 1000

print(cuenta.depositar(500))    # True
print(cuenta.saldo)             # 1500

print(cuenta.retirar(200))      # True
print(cuenta.retirar(5000))     # False — fondos insuficientes
print(cuenta.saldo)             # 1300

# Titular de solo lectura
try:
    cuenta.titular = "Otro"
except AttributeError as e:
    print(f"Error: {e}")

# Saldo negativo
try:
    cuenta.saldo = -100
except ValueError as e:
    print(f"Error: {e}")