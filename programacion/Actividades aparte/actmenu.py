import math

print("Este programa calcula el area de figuras geometricas")
menuInicio= '''
******************************************
*                .Triangulo              *
*                .Rectangulo             *
*                .Circunferencia         
*                .Salir                       *
******************************************
'''
print(menuInicio)
import math 
def Rectangulo():
    Altura = float(input("Ingrse la altura del rectangulo: "))
    Base = float(input("Ingrese la base del rectangulo: "))
    Area = Altura * Base 
    print("El area del rectangulo es: ", Area)

def Triangulo():
    Altura = float(input("Ingrse la altura del triangulo: "))
    Base = float(input("Ingrese la base del triangulo: "))
    Area = Altura * Base /2 
    print("El area del triangulo es: ", Area)

def Circunferencia():
    Radio = float(input("Ingrse el radio del circunferencia: "))
    math.pi
    Area = math.pi * Radio **2
    print("El area del circunferencia es: ", Area)

def menu():
    print(menu)
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        Triangulo()
    elif opcion == 2:
        Rectangulo()
    elif opcion == 3:
        Circunferencia()
    elif opcion == 4:
        exit()

print (menu())

print("Fin del programa")