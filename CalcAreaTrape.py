#Calcular Area del Trapecio
import math
def CalculaTrape (altura,base1,base2):
    print((altura * ((base1 + base2) / 2) ))

altura = int(input("Ingresa la altura del Trapecio: "))
base1  = int(input("Ingresa la base1 del Trapecio: "))
base2  = int(input("Ingresa la base2 del Trapecio: "))

CalculaTrape (altura,base1,base2)
