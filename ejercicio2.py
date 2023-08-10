print('*'*10)
print('BIENVENIDO')
print('*'*10)
print('Hallaremos medidas claves de tus cuadrados o rectangulos')
nombre = input('cual es tu nombre => ')
def juego():
    print(f'Vamos a empezar {nombre}')
    altura = float(input('Ingresa la altura => '))
    base = float(input('Ingresa la base => '))

    perimetro = (altura*2) + (base*2)
    area = base * altura
    if altura == base:
        print(f'El perimetro de tu cuadrado es {perimetro} y el area es {area}')
    else:
        print(f'El perimetro de tu rectangulo es {perimetro} y el area es {area}')
juego()

while True:
    eleccion = input('Deseas probar con otras medidas? ').lower()
    if eleccion == 'si' or eleccion == 'yes':
        juego()
    else:
        print('Gracias por probar')
        break