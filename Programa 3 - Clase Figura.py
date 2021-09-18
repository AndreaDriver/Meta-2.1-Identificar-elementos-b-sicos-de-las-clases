"""""
DESCRIPCION: Clase figura con tres hijos
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 14/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

from abc import ABC, abstractmethod
from math import sqrt
from math import pi

class Figura(ABC):

    def __init__(self):
        self.tipo = ""

    def setTipo(self,tipo):
        self.tipo = tipo

    def getTipo(self,tipo):
        return  self.tipo

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    def __str__(self):
        return "Tipo: ", self.tipo

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        Figura.setTipo(self,"Triangulo")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3


    def calcularPerimetro(self):
        self.perimetroT =round(self.lado1+self.lado2+ self.lado3,2)

    def calcularArea(self):

        if self.lado1 == self.lado2 and self.lado2 == self.lado3: #equilatero
            self.areaT = round(((sqrt(3) / 4)) * (self.lado1 ** 2), 2)
            self.tipoTriangulo = "Equilatero"
        elif self.lado1 != self.lado2 and self.lado3 != self.lado2 and self.lado1 != self.lado3: #escaleno
            self.semiP = self.perimetroT /2
            self.areaT =  round(sqrt(self.semiP * (self.semiP - self.lado1) * (self.semiP - self.lado2) * (self.semiP - self.lado3)),2)
            self.tipoTriangulo = "Escaleno"
        else: #isoceles
            if self.lado1 == self.lado2: #3
                self.areaT =  round((self.lado3 * sqrt((self.lado1**2) - ((self.lado3 ** 2) / 4)))/2,2)
                self.tipoTriangulo = "Isósceles"
            elif self.lado1 == self.lado3:#2
                self.areaT = round((self.lado2 * sqrt((self.lado1 ** 2) - ((self.lado2 ** 2) / 4))) / 2, 2)
                self.tipoTriangulo = "Isósceles"
            elif self.lado2 == self.lado3:#1
                self.areaT = round((self.lado1 * sqrt((self.lado2 ** 2) - ((self.lado1 ** 2) / 4))) / 2,2)
                self.tipoTriangulo = "Isósceles"

    def __str__(self):
        return "Tipo: {}, Área: {}, Perimetro: {}, Tipo de triangulo: {}".format(self.tipo, self.areaT, self.perimetroT, self.tipoTriangulo)

class Circulo(Figura):

    def __init__(self, radio):
        Figura.setTipo(self,"Circulo")
        self.radio = radio

    def calcularArea(self):
        self.areaC = round(pi * (self.radio**2),2)

    def calcularPerimetro(self):
        self.perimetroC =round(2*pi*self.radio,2)

    def __str__(self):
        return "Tipo: {}, Área: {}, Perimetro: {}".format(self.tipo, self.areaC, self.perimetroC)

class Rectangulo(Figura):
    def __init__(self, ancho, largo):
        Figura.setTipo(self,"Rectangulo")
        self.ancho = ancho
        self.largo = largo

    def calcularArea(self):
        self.areaR = round(self.ancho * self.largo, 2)

    def calcularPerimetro(self):
        self.perimetroR = round((self.ancho*2)+(self.largo*2), 2)

    def __str__(self):
        return "Tipo: {}, Área: {}, Perimetro: {}, ".format(self.tipo, self.areaR, self.perimetroR)

for figura in Circulo(3), Triangulo(3,2,3), Rectangulo(2,8):
    figura.calcularPerimetro()
    figura.calcularArea()
    print(figura.__str__())