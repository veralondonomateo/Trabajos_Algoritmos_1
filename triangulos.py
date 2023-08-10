
def triangulos():
    print('Bienvenido')
    print('calculadora de triangulos')
    elecciona = input('ingresa el lado a del triangulo => ')
    eleccionb = input('ingresa el lado b del triangulo => ')
    eleccionc = input('ingresa el lado c del triangulo => ')
    if (elecciona == eleccionb) == eleccionc:
        print('es un triangulo equilatero')
    elif elecciona + eleccionb < eleccionc or elecciona + eleccionc < eleccionb or eleccionb + eleccionc < elecciona:
        print('el triangulo no existe')
    elif elecciona == eleccionb or eleccionb == eleccionc or elecciona == eleccionc:
        print('es un triangulo isoceles')
    elif eleccionc != elecciona != eleccionb or eleccionb != elecciona:
        print('es un triangulo escaleno')
    

triangulos()
while True:
    eleccion = input('deseas probar con otro triangulo')
    eleccion = eleccion.lower
    if eleccion == 'si':
        break
    else:
        triangulos()