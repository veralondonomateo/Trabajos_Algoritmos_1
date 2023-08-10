import random

print('Bienvenido a mathtest')
print('Responderas algunas preguntas')
usuario = input('Ingrese su nombre de usuario: ')

respuestas_correctas = 0
cantidad_de_respuestas = 0 
diccionario = {'¿Cuál es el valor de π (pi) en dos cifras?': '3.14'
               , '¿Cuántos grados tiene un triángulo equilátero?': '3'
               ,'¿Cuánto es la raíz cuadrada de 25?': '5' , 
               '¿Cuánto es el resultado de 12 dividido por 4?': '3',
                '¿Cuánto es el producto de 6 por 8?': '48', 
                '¿Cuál es el número primo más pequeño?': '2' ,
                '¿Cuánto es el área de un círculo con radio 3?': '28.7'}


while True:
    for i in diccionario.keys():
        print(i)
        respuesta = input()
        if respuesta == diccionario[i]:
            print('Acertaste')
            respuestas_correctas += 1
            cantidad_de_respuestas += 1
        else:
            print('Erraste')
            cantidad_de_respuestas += 1

    if cantidad_de_respuestas == 7:
         break

respuestas_correctas1 =round((respuestas_correctas / 7) * 100)  
print(f'{usuario} acertaste en un {respuestas_correctas1}%')
notas = []
notas.append(respuestas_correctas1)
print(notas)




