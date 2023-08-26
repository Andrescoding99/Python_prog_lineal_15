"""•	Ingrese un conjunto de tres notas de examenes y laboratorios Sabiendo que, tanto las tres 
notas de sus exámenes y las tres de sus laboratorios tienen un valor de 35% de su nota final, 
cuanto deberá obtener en su proyecto final para poder pasar el módulo con una nota final de 8.0. 
mostrar en pantalla, nota final obtenida en su examen y laboratorio, finalmente, la nota necesaria para aprobar su modulo."""

#Declarando variables

tP = 0 # Esto es la nota total de los parciales
tL = 0 # Esto es la nota total de los laboratorios
tPL = 0 #Esto es la suma de los parciales y laboratorios
tPr = 0 #Esto es el total proyecto
tM = 0 #Esto es lo necesesario para pasar el modulo

temp = 0

techo1 = 0
techo2 = 3

# Declarando vectores

x = [] #Notas de parciales
y = [] # Notas de laboratorios

#Declarando acumuladores

acuA = []
acuB = []
acuC = []

# Declarando iteradores

i = 0
j = 0
k = 0


print("Notas de estudiante")

#Ingreso de nota de parciales

i = 3
for j in range (i):
    x.append(float(input("Ingresa la nota del parcial {}:  ".format(j+1))))
    while x[j] < 1 or x[j] > 10:
        print("Ha ingresado un valor fuera del rango, intente otra vez\n")
        x[j] = float(input("Ingresa la nota del parcial {}:  ".format(j+1)))
    print("Valor aceptado\n")

    y.append(float(input("Ingresa la nota del laboratorio {}:  ".format(j+1))))
    while y[j] < 1 or y[j] > 10:
        print("Ha ingresado un valor fuera del rango, intente otra vez\n")
        y[j] = float(input("Ingresa la nota del laboratorio {}:  ".format(j+1)))
    print("Valor aceptado\n")


print("\nNota parciales")

for j in range (techo1, techo2):
    tP = x[j] + tP

tP = (tP/3) * 0.35

print("Nota final parciales: {}".format(round(tP,1)))

print("\nNota laboratorios")

for j in range (techo1, techo2):
    tL = y[j] + tL

tL = (tL/3) * 0.35

print("Nota final laboratorio: {}".format(round(tL,1)))

#Suma de ambas notas

tPL = tP + tL

if tPL < 5:
    print("Es imposible pasar con 8 el modulo, ya que ni la nota maxima llegaria a 8")
else:
    tPr = 8 - tPL
    tM = (tPr * 10) / 3

    print("Nota obligatoria para pasar con 8: {}".format(round(tM,1)))

#Nota estuve usando la aproximacion, asi que no estoy seguro cuando si y cuando NO
