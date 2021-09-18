"""""
DESCRIPCION: Clase persona con dos hijos que la heredan
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 14/09/21
ULTIMA MODIFICACION: 17/19/21
"""""

class Persona:

    #constructor
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    #metodos get y set
    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self._apellido

    def setNombre(self, nombre):
        self._nombre = nombre

    def setApellido(self, apellido):
        self._apellido = apellido

    def __str__(self):
        print("Nombre: {}, Apellido: {}".format(self._nombre, self._apellido))

class Profesor(Persona):

    def __init__(self, nombre, apellido, despacho):
        Persona.__init__(self,nombre, apellido)
        self._despacho = despacho

    # metodos get y set
    def getDespacho(self):
        return self._despacho
    def setDespacho(self, despacho):
        self._despacho = despacho

    def __str__(self):
        print("Nombre: {}, Apellido:{}, despacho: {}".format(self._nombre, self._apellido, self._despacho))

class Alumno(Persona):

    def __init__(self, nombre, apellido, semestre):
        Persona.__init__(self, nombre, apellido)
        self._semestre = semestre

    # metodos get y set
    def getSemestre(self):
        return self._semestre

    def setSemestre(self, semestre):
        self._semestre = semestre

    def __str__(self):
        print("Nombre: {}, Apellido:{}, semestre: {}".format(self._nombre, self._apellido, self._semestre))


for personas in Alumno("Betty","Pinzon","9"), Profesor("Mario", "Calderon", "101"):
    personas.__str__()