"""•	Un estudiante desea conocer el promedio final de su materia de matemáticas, para ello 
deberá capturar notas de tres exámenes, tres laboratorios y nota de proyecto trimestral, deberá 
capturar dichos datos para tres trimestres, mostrar en pantalla, nota final para cada trimestre, 
nota final de la materia y su nombre. Tomar en cuenta que los exámenes y laboratorios tienen un 
valor de 35% cada uno respectivamente y el proyecto únicamente un 30% para cada trimestre """

# Declarando variables

temp = 0

# Declarando acumulador

acuA = []
acuB = []
acuC = [] 

# Trimestre 1 
techo1 = 0 
techo2 = 3

# Trimestre 2
techo3 = 3
techo4 = 6

# Trimestre 3
techo5 = 6
techo6 = 9

# Declarando vectores

x = [] # Vector para examenes
y = [] # Vector para laboratorios
z = [] # Vector para proyecto

# Declarando iteradores

i = 0
j = 0 
k = 0
l = 0

#Nota, poner que i valga 2


print ("Promedio final de estudiante")

print("Ingreso de valores de notas de examenes")

i = 9

#Primera forma, de como meter valores con validacion en un vector

for j in range (i):
    temp = float(input("Ingresa la nota de su examen numero {}: ".format(j+1)))
    while temp < 0.01 or temp >= 10.01:
        print("El nota que ingresó esta fuera del rango de lo permitido, intente de nuevo")
        temp = float(input("Ingresa la nota de su examen numero {}: ".format(j+1)))
    print("Valor aceptado\n")
    x.append(temp)

print("Ingreso de valores de notas de laboratorios")

#Segunda forma, de como meter valores con validacion en un vector


for k in range (i):
    y.append(float(input("Ingresa la nota de su laboratorio numero {}: ".format(k+1))))
    while y[k] < 0.01 or y[k] >= 10.01:
        print("La nota que ingresó esta fuera del rango de lo permitido, intente otra vez")
        y[k] = float(input("Ingresa la nota de su laboratorio numero {}: ".format(k+1)))
    print("Valor aceptado\n")

temp = 0

print("Ingreso de valores de notas de proyectos")

i = 3

for l in range (i):
    temp = float(input("Ingresa la nota de su proyecto numero {}: ".format(l+1)))
    while temp < 0.01 or temp >= 10.01:
        print("La nota que ingresó esta fuera del rango de lo permitido, intente de nuevo")
        temp = float(input("Ingresa la nota de su proyecto numero {}: ".format(j+1)))
    print("Valor aceptado\n")
    z.append(temp)


print("Resultados obtenidos")

print("-----------------------------------------------------------------")

print("Resultados de examenes")

#Primer trimestre

temp = 0

for j in range(techo1, techo2):
    temp = x[j] + temp 

temp = (temp / 3)* 0.35

acuA.append(temp)


#Segundo trimestre

temp = 0

for j in range(techo3, techo4):
    temp = x[j] + temp 

temp = (temp / 3)* 0.35

acuA.append(temp)

#Tercer trimestre

temp = 0

for j in range(techo5, techo6):
    temp = x[j] + temp 

temp = (temp / 3)* 0.35

acuA.append(temp)


print("-----------------------------------------------------------------")

print("Resultados de laboratorios")

temp = 0

for j in range(techo1, techo2):
    temp = y[j] + temp 

temp = (temp / 3)* 0.35

acuB.append(temp)


#Segundo trimestre

temp = 0

for j in range(techo3, techo4):
    temp = y[j] + temp 

temp = (temp / 3)* 0.35

acuB.append(temp)

#Tercer trimestre

temp = 0

for j in range(techo5, techo6):
    temp = y[j] + temp 

temp = (temp / 3)* 0.35

acuB.append(temp)

print("-----------------------------------------------------------------")

print("Resultados de proyectos")

for j in range(techo1, techo2):
    acuC.append(z[j]* 0.30)

print("-----------------------------------------------------------------")

temp = 0

for j in range(i):
    print("Nota final, trimestre {}: {}".format(j+1,acuA[j] + acuB[j] + acuC[j]))
    temp = temp + (acuA[j] + acuB[j] + acuC[j])

print("Nota final total: {}".format(temp/3))

if (temp/3) > 5.99:
    print("Usted ha aprobado matematica")
else:
    print("Usted ha reprobado matematica")