"""""
DESCRIPCION: clase Punto (con atributos x e y) y cuatro metodos
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 14/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
import math


class Punto:
    import math

    #constructor
    def __init__(self):
        self.y2 = ""
        self.x2 = ""

    #metodos set
    def set_x2(self, xx2):
        self.x2 = xx2

    def set_y2(self, yy2):
        self.y2 = yy2

    #metodos get
    def get_x(self):
        return self.x2

    def get_y(self):
        return self.y2

    #metodo distancia a 0
    def distanceToZero(self):
        self.distancia_a_cero = math.sqrt(((self.x2 - 0)**2) + ((self.y2 - 0)**2))
        return self.distancia_a_cero

    #metodo distancia entre x,y a otro punto
    def distance(self, xother, yother):
        self.distancia_a_otro = math.sqrt(((self.x2 - xother) ** 2) + ((self.y2 - yother) ** 2))
        return self.distancia_a_otro

    #metodo, cual esta mas lejos de (0,0)
    def squaredDistanceToZero(self, xo1, yo1):
        self.distancia_a = math.sqrt(((self.x2 - 0) ** 2) + ((self.y2 - 0) ** 2))
        self.distancia_b = math.sqrt(((xo1 - 0) ** 2) + ((yo1 - 0) ** 2))

        if self.distancia_a == self.distancia_b:
            self.distanciaMasCorta = "Ambos distancias son iguales"
        else:
            if self.distancia_a < self.distancia_b:
                self.distanciaMasCorta = "Punto 1"
            else:
                self.distanciaMasCorta = "Punto 2"
        return  self.distanciaMasCorta

    def __str__(self):
        return "Las coordenadas del punto 1 son --> x({}), y({})".format(self.x2, self.y2)


p1 = (input("Ingresa punto 1 (x,y): ")) #1,5
p2 = (input("Ingresa punto 2 (x,y): ")) #1,6

punto = Punto
punto.set_x2(punto, int(p1[0]))
punto.set_y2(punto,int(p1[2]))

print(punto.__str__(punto))
print("La distancia entre punto 1 a 0,0 es --> {:.2f}".format(punto.distanceToZero(punto)))
print("La distancia entre el punto 1 y 2 es --> {:.2f}".format(punto.distance(punto,int(p2[0]),int(p2[2]))))
print("El punto mas cercano al punto (0,0) es el --> ", punto.squaredDistanceToZero(punto,int(p2[0]),int(p2[2])))
print("La distancia entre el punto 1 y el (0,0) es --> {:.2f} \nLa distancia entre el punto 2 y el (0,0) es --> {:.2f}".format(punto.distancia_a, punto.distancia_b))