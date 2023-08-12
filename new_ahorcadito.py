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
        break

    




#Ponemos este código para que solo se ejecute cuando llamamos al archivo

    

