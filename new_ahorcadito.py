
'''import random
esquema = [
      +---+
      |   |
          |
          |
          |
          |
    =========,
      +---+
      |   |
      O   |
          |
          |
          |
    =========,
      +---+
      |   |
      O   |
      |   |
          |
          |
    ========, 
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========, 
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========, 
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========, 
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========]

lista_palabras = ['colombia','venezuela','brazil','ecuador','peru',"estados unidos", "canadá", "méxico", "argentina", "españa", "francia", "alemania", "China", "Japón", "India", "Australia", "Rusia", "Italia", "Reino Unido", "Sudáfrica", "Egipto", "Nigeria", "Kenia", "Corea del Sur"]

#Elegimos la palabra de forma aleatoria
def eleccion():
    lista = random.choice(lista_palabras)
    lista_ = lista.lower()
    return lista_
eleccion_v1 = eleccion()
eleccion_v2 = list(eleccion_v1)
print(eleccion_v2)

print('*'*10)
print('Bienvenidos al ahorcado de mateo')
print('*'*10)
letras = []
erroneas = []


tablero = ["_"] * len(eleccion_v1)




while True:
    print(eleccion_v1)
    eleccion_persona = input('Elige una letra => ')
    
    

    if eleccion_persona in eleccion_v1:
        letras.append(1)
    
    if eleccion_persona not in eleccion_v1:
        erroneas.append(eleccion_persona)
        print('Te equivocaste, intenta de nuevo ')
    for i in erroneas:
        print('Letras erroneas')
        print(i)
    if len(letras) == len(eleccion_v2):
        print('Ganaste')
        break'''
import time 
import random  
print('*'*10)
print('Bienvenido al ahorcadito')
print('*'*10)
name = input('¿Cúal es tu nombre? ')
time.sleep(1.5)
print(f'Hola {name} comencemos a jugar')
lista = ('colombia','venezuela','brazil','ecuador','peru',"estados unidos", "canadá", "méxico", "argentina", "españa", "francia", "alemania", "China", "Japón", "India", "Australia", "Rusia", "Italia", "Reino Unido", "Sudáfrica", "Egipto", "Nigeria", "Kenia", "Corea del Sur")
palabra = random.choice(lista)
tupalabra = ''
vidas = 5
while vidas > 0:
    fallas = 0
    for letra in palabra:       
        if letra in tupalabra:
            print(letra, end='')
        else:
            print('_',end='')
            fallas += 1
    if fallas == 0:
        print('\nGANASTE')
        break
    tuletra = input('\n Elige una letra => ')
    tupalabra += tuletra

    if tuletra not in palabra:
        print('LETRA INCORRECTA')
        vidas -= 1
        print(f'Te quedan {vidas} vidas')

if vidas == 0:
    print('Perdiste, Lo sentimos')
    



    

