import random
esquema = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

lista_palabras = ['colombia','venezuela','brazil','ecuador','peru',"estados unidos", "canadá", "méxico", "argentina", "españa", "francia", "alemania", "China", "Japón", "India", "Australia", "Rusia", "Italia", "Reino Unido", "Sudáfrica", "Egipto", "Nigeria", "Kenia", "Corea del Sur"]

#Elegimos la palabra de forma aleatoria
def eleccion():
    lista = random.choice(lista_palabras)
    lista_ = lista.lower()
    return lista_
eleccion_v1 = eleccion()
eleccion_v2 = set(eleccion_v1)
print(eleccion_v2)

print('*'*10)
print('Bienvenidos al ahorcado de mateo')
print('*'*10)
letras = []
letras_ = set(letras)
repetidas = []
tablero = ["_"] * len(eleccion_v1)




while True:
    print(eleccion_v1)
    eleccion_persona = input('Elige una letra => ')
    print(letras)
    
    if letras_ :
        print('Ganaste')
        break
    elif eleccion_persona in eleccion_v1:
        letras.append(eleccion_persona)
    elif eleccion_persona not in eleccion_v1:
        print('Letra erronea')

    





#Ponemos este código para que solo se ejecute cuando llamamos al archivo

    

