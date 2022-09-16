class Persona:
    def _init_(self,nombre,edad)-> None:
        self.nombre = nombre
        self.edad = edad
    def __str__(self) -> str:
        return f"Persona{self.nombre}{self.edad}"

class Empleado(Persona):
    def _init_(self, nombre, edad, sueldo):
        super()._init_(nombre,edad)
        self.sueldo = sueldo
    def str(self) -> str:
        return f"{super()}"

miEmpleado = Empleado("Pedro",24,500)

print(miEmpleado.Nombre)