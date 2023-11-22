#Ticiana Passalacqua Gyurkovits

class Rectangulo :

    def __init__ (self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area (self):

        self.area = self.longitud * self.ancho
        return (self.area)

    def calcular_perimetro (self):

        self.perimetro = self.longitud + self.ancho * 2 
        return (self.perimetro)

#rec1 = Rectangulo (6,8)

#print (rec1.calcular_perimetro())
