# Función para asignar las elecciones y acceder al resultado
def triangulos():
    print('Bienvenido')
    print('calculadora de triangulos')
    elecciona = input('ingresa el lado a del triangulo => ')
    eleccionb = input('ingresa el lado b del triangulo => ')
    eleccionc = input('ingresa el lado c del triangulo => ')

    #Condicionales
    if (elecciona == eleccionb) == eleccionc:
        print('es un triangulo equilatero')
    elif elecciona + eleccionb < eleccionc or elecciona + eleccionc < eleccionb or eleccionb + eleccionc < elecciona:
        print('el triangulo no existe')
    elif elecciona == eleccionb or eleccionb == eleccionc or elecciona == eleccionc:
        print('es un triangulo isoceles')
    else:
        print('es un triangulo escaleno')
    
#Llamado de la función
triangulos()

#Repetición del ciclo para preguntar si el usuario desea repetir el proceso
while True:
    eleccion = input('deseas probar con otro triangulo')
    eleccion = eleccion.lower

    #Momento de elección

    if eleccion == 'si':
        #Rompiendo el código
        break
    else:
        triangulos()