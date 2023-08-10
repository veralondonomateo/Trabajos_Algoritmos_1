#Importamos la libreria functools para hacer reducciones dentro de listas
import functools
print('BIENVENIDOS')
print('CALCULA EL PROMEDIO DE TUS NOTAS UNIVERSITARIAS')

#Preguntamos la cantidad de materias que el usuario tiene
materias = int(input('Cuantas materias tienes este semestre? '))

#Creamos dos listas vacias en las cuales se guardaran las notas y los creditos
notas =[]
creditos = []

#Iniciamos un ciclo while que se ejecutara hasta que procese todas las materias que el usuario ingreso

while materias > 0:

    #En cada vuelta le restaremos uno a la varible 'materias' para procesar la cantidad total de materias ingresadas por el usuario
    #Cuando la variable 'materias' sea cero el ciclo se rompe
    materias -= 1

    #Pregunta la nota de la materia y la asigna a la lista global 'notas' con el método .append
    materia = float(input('Ingresa la nota de la materia=> '))
    notas.append(materia)

    #Pregunta la cantidad de creditos y la asigna a la lista global 'creditos' con el método .append
    creditos1 = float(input('Ingresa la cantidad de creditos de esta materia =>\n'))
    creditos.append(creditos1)

#Busca dentro de las listas notas y creditos y multiplica posición por posición y lo almacena en la lista 'multiplicacion_notas'
multiplicacion_notas = list(map(lambda x,y : x*y, notas, creditos ))

# Suma todos los elementos de la lista 'multiplicacion_notas' con el método .reduce y una función lambda
multiplicacionnotasreduce = functools.reduce(lambda p,q : p + q, multiplicacion_notas)

#Suma los elementos dentro de la lista 'creditos' con el método .reduce y una función lambda
creditosreduce = functools.reduce(lambda p,q : p + q ,creditos)

#Divide los dos resultados anteriores
resultado_total = multiplicacionnotasreduce / creditosreduce

#En resultado_total se almacena el promedio final
resultadototal_v2 = f'Tu promedio total es {resultado_total}'
print(resultadototal_v2)