# Meta-2.1-Identificar-elementos-b-sicos-de-las-clases
M2.1 Vara Andrea
Crear la clase Punto (con atributos x e y) con los siguientes métodos (a parte de constructor, getters y setters):
distanceToZero()  # distancia entre self y (0, 0)
distance(Point other)  # distancia entre self y other
squaredDistanceToZero() # sirve para comparar distancias 
__str__  #  Imprimir punto. Ejemplo: (x, y) 

Crear una clase llamada Persona (con nombre y apellidos como atributos) y dos clases que hereden de Persona: Profesor (con atributo adicional String despacho) y Alumno (con atributo adicional String semestre). Los atributos de las tres clases deben ser protected. Las tres clases sobrescribirán el método __str__ de tal forma que las clases hijas invoquen el método de la clase padre. El __str__ de Persona mostrará “apellido, nombre”, el de Alumno lo mismo seguido del semestre y el de Profesor seguido de su despacho. Las tres clases tendrán como mínimo el constructor y el __str__, además debe incluir sus respectivos set y get para cada atributo. Finalmente, crear objetos de estas clases que imprima sus valores, para que se vea que en cada caso se invoca el __str__ que corresponde.

Crear una clase Figura con un atributo de tipo String llamado “tipo” (que podrá ser “Triángulo”, “Círculo”, “Rectángulo”, etcétera. A parte del constructor y del __str__ tendrá dos métodos abstractos(@abstractmethod): calcularArea() y calcularPerimetro() que devolverán el área y el perímetro de la figura. Crearemos tres clases hijas de Figura: Triangulo (Agregar atributo de longitud lado 1, longitud lado 2, longitud lado 3), Circulo (Agregar atributo radio) y Rectangulo (agregar atributo ancho y largo). Cada clase sobreescribirá los metodos abstractos los cuales tienen que calcular su área y perímetro correspondiente. Crearemos los objetos necesarios para comprobar que funcionan correctamente.
