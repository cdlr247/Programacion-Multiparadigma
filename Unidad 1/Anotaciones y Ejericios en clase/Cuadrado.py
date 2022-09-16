from FiguraGeom import FiguraGeometrica
from Color import color

class Cuadrado(FiguraGeometrica,Color):
    def _init_(self,ancho,alto) -> None:
        FiguraGeometrica._init_(self,lado,lado)
        Color._init_(self,color)
    def CalcularArea(self):
        return self.alto * self.ancho
        #super()._init_(ancho,alto)