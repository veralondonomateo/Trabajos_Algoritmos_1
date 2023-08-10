#Juego de preguntados
"""print('¡PREGUNTADOS!')
#Escogencia de la tematica a jugar
#Deportes  #Historia #Matemáticas

import random

Deporte= {
    '¿Cuantos mundiales tiene brazil? ' : '5',
    '¿En que año se originaron los juegos olimpicos?' : '776AC',
    '¿Cuánto dura un partido de fútbol?' : '90',
    '¿Cuánto dura la prórroga en un partido de fútbol? ' : '30',
    '¿Cuáles son las tres grandes vueltas del ciclismo?' : 'el tour de francia, la vuelta a españa y el giro de italia',
    '¿Qué equipo de la Premier League tiene más ligas ganadas?' : 'manchester united',
    '¿Quién se considera el mejor jugador de baloncesto de todos los tiempos?' : 'michael jordan',
    '¿Cual es la bicrosista mas famosa de Colombia?' : 'mariana pajon',
    '¿Cada cuántos años se celebran los Juegos Olímpicos? ': '4'
}

#Imprime todos los valores de el diccionario deportes
for i in Deporte():
    print (i)

#Geografía
Geografia = {
    '¿Cuál es el río más largo de la Península Ibérica?' : 'rio tajo',
    '¿Cuál es el país más pequeño del mundo?' : 'cuidad del vaticano' , 
    '¿Cuántos océanos hay en la Tierra?' : '5',
    '¿Como se llama el rio mas grande del mundo ' : 'nilo',
    '¿Cuál es el país más grande del mundo por área terrestre?' : 'rusia',
    '¿Cuál es el desierto más grande del mundo?': 'sahara' ,
    '¿Cuál es el país más pequeño del mundo?' : 'Vaticano',
    '¿Cuál es la cadena montañosa más larga de América?' : 'los andes' , 
    '¿Cuál es el país más poblado del mundo?' : 'china'
}
#Imprime cada valor de el diccionario geografia1
for i in Geografia():
    print(i)

#Historia
Historia = {
    '¿En qué año ocurrió la Revolución Francesa?' : '1789' ,
    '¿Quién fue el líder de la Revolución Rusa de 1917?': 'vladimir lenin',
    '¿Cuándo terminó la Segunda Guerra Mundial?' : '1945',
    '¿Qué evento histórico ocurrió el 12 de octubre de 1492?' : 'cristóbal colón llegó a américa',
    '¿Quién fue el primer presidente de los Estados Unidos?' : 'George Washington',
    '¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?' : '1776',
    '¿Cuándo comenzó la Revolución Industrial?' : '1760',
    '¿Cuál fue el imperio más extenso de la historia?' : 'el imperio británico ',
    '¿En que año cayó el Muro de Berlín?': '1989',
    '¿Quién fue el líder de la Revolución Cubana en 1959?': 'fidel castro'
} 

#Imprime cada valor de el diccionario historia
for i in Historia():
    print(i)

Matematicas = {
    '¿Cuál es el valor exacto de la constante áurea (phi)?' : '1.6',
    '¿Cuál es la probabilidad de obtener tres caras consecutivas al lanzar una moneda justa?' : '0.125',
    'Cual es la derivada de una constante' : '0',
    '¿Cuál es el valor de "e" elevado a la potencia de pi veces i? ' : '-1',
    '¿Cuánto es el área de un cuadrado con lados de longitud 6?' : '36',
    '¿Cuál es el resultado de multiplicar 5 por 3 y luego restarle 2?' : '13',
    '¿Un numero positivo elevado a la cero es igual?' : '1',
    '¿Cual es la derivada de cosx?' : '-senx'
}

#Imprime cada valor del diccionario Matemáticas
for i in Matematicas():
    print(i)




# Cada variable nos va a dar un elemento aleatorio del diccionario
eleccion_deporte = random.choice(list(Deporte.keys()))
eleccion_geografia = random.choice(list(Geografia.keys()))
eleccion_matematicas = random.choice(list(Matematicas.keys()))
eleccion_Historia = random.choice(list(Historia.keys()))


if clave_aleatoria == mi_diccionario[clave_aleatoria]:
# Empezamos con la impresion del juego
print('Elige un sector para las preguntas')
print('1- Deporte')
print('2-Geografia')
print('3-Historia')
print('4-Matemáticas')

deseo_del_jugador = int(input())
vidas = 3
estrellas = 0

# Ciclo para la eleccion del diccionario Deportes
if deseo_del_jugador == 1:
    print('\nBIENVENIDO A LA SECCION DE DEPORTES\n')
    print('Si aciertas a una pregunta sumas una estrella si no pierdes una vida ')
    while vidas > 0 and estrellas < 3:  
        print(f'Tienes {vidas} vidas y {estrellas} estrellas \n') 
        eleccion_deporte = random.choice(list(Deporte.keys()))
        print(eleccion_deporte)
        respuesta = input()
        if respuesta == Deporte[eleccion_deporte]:
            estrellas += 1
            print(f'Es correcto, tienes {estrellas} estrellas')
        else:
            vidas -= 1
            respuestacorrecta = Deporte[eleccion_deporte]
            print(f'La respuesta correcta era {respuestacorrecta} ')
            print(f'te equivocaste, te quedan {vidas} vidas')
        if vidas == 0:
            print('Perdiste :(')
        elif estrellas == 3:
            print('Ganaste, Felicitaciones :)')

# Ciclo para la sección de geografía 
if deseo_del_jugador == 2:
    print('BIENVENIDO A LA SECCION DE GEOGRAFÍA\n')
    print('Si aciertas a una pregunta sumas una estrella si no pierdes una vida ')
    while vidas > 0 and estrellas < 3:
        print(f'Tienes {vidas} vidas y {estrellas} estrellas')
        eleccion_geografia = random.choice(list(Geografia.keys()))
        print(eleccion_geografia)
        respuesta = input()
        if respuesta == Geografia[eleccion_geografia]:
            estrellas += 1
            print(f'Acertaste! Tienes {estrellas} estrellas y {vidas} vidas')
        else:
            vidas -= 1 
            respuestacorrecta = Geografia[eleccion_geografia]
            print(f'La respuesta correcta era {respuestacorrecta} ')
            print(f'Te equivocaste! Te quedan {vidas} vidas y tienes {estrellas} estrellas')
        if vidas == 0:
            print('Perdiste :(')
        elif estrellas == 3:
            print('Felicidades, Ganaste!')


# Ciclo para la sección de historia
if deseo_del_jugador == 3:
    print('BIENVENIDO A LA SECCIÓN DE HISTORIA')
    print('Si aciertas a una pregunta sumas una estrella si no pierdes una vida ')
    while vidas > 0 and estrellas < 3:
        print(f'Tienes {vidas} vidas y {estrellas} estrellas \n')
        eleccion_Historia = random.choice(list(Historia.keys()))
        print(eleccion_Historia)
        respuesta = input()
        if respuesta == Historia[eleccion_Historia]:
            estrellas += 1
            print(f'Acertaste! Tienes {estrellas} estrellas')
        else : 
            vidas -= 1
            respuestacorrecta = Historia[eleccion_Historia]
            print(f'La respuesta correcta era {respuestacorrecta} ')
            print(f'Te equivocaste! te quedan {vidas} vidas')
        if vidas == 0:
            print('Perdiste')
        elif estrellas == 3:
            print('Felicidades, Ganaste :)')


# Ciclo para la eleccion del diccionario Matematicas
if deseo_del_jugador == 4:
    print('\nBIENVENIDO A LA SECCION DE MATEMÁTICAS \n')
    print('Si aciertas a una pregunta sumas una estrella si no pierdes una vida ')
    while vidas > 0 and estrellas < 3:  
        print(f'Tienes {vidas} vidas y {estrellas} estrellas \n') 
        eleccion_matematicas = random.choice(list(Matematicas.keys()))
        print(eleccion_matematicas)
        respuesta = input()
        if respuesta == Matematicas[eleccion_matematicas]:
            estrellas += 1
            print(f'Es correcto, tienes {estrellas} estrellas')
        else:
            vidas -= 1
            respuestacorrecta = Matematicas[eleccion_matematicas]
            print(f'La respuesta correcta era {respuestacorrecta} ')
            print(f'te equivocaste, te quedan {vidas} vidas')
        if vidas == 0:
            print('Perdiste :(')
        elif estrellas == 3:
            print('Ganaste, Felicitaciones :)')"""

# Facetas de un string y cambios en sus metodos

# Cambio de todo a minuscula






