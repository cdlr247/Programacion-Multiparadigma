class Rectangulo:
    def __init__(self,ancho,largo) -> None:
        self._ancho = ancho
        self._largo = largo
    def CalcularPerimetro(self):
        return self._ancho * self._largo



class Cuadrado:
    def __init__(self,lado) -> None:
        self._lado = lado
    def Area (self):
        return(self._lado * self._lado)
        