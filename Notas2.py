"""•	Un estudiante universitario, ha obtenido como notas en sus parciales 8, 10, 8, y en sus 
laboratorios las notas son  de 9, 8, 8. Sabiendo que, tanto las tres notas de sus exámenes y las 
tres de sus laboratorios tienen un valor de 35% de su nota final, cuanto deberá obtener en su 
proyecto final para poder pasar el módulo con una nota final de 8.0. mostrar en pantalla, nota 
final obtenida en su examen y laboratorio, finalmente, la nota necesaria para aprobar su modulo."""

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

x = [8,10,8] #Notas de parciales
y = [9,8,8] # Notas de laboratorios

#Declarando acumuladores

acuA = []
acuB = []

# Declarando iteradores

i = 0
j = 0
k = 0


print("Notas de estudiante")


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
