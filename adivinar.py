'''import random
def adivinar():
    

    print('Bienvenido a las adivinanzas')
    print('Debes adivinar un numero entre 1 y 100')
    num_adivinar = random.choice(range(1,101))
    vidas = 4
    while True:
        #Ciclo infinito hasta la adivinación del número a encontrar
        eleccion = int(input('elige un numero => '))
        vidas -= 1
        if eleccion > 100 : 
            print('Recuerda que el número a adivinar esta entre 1 y 100')
        elif eleccion == num_adivinar:
            print('¡FELICIDADES! Adivinaste')
            break
        elif eleccion < num_adivinar:
            print('Es un número mayor')
        elif eleccion > num_adivinar:
            print('Es un numero menor') 
        elif vidas == 0:
            print('Perdiste, chao')
            break
        
adivinar()
while True:
    #Ciclo infinito para la toma de decisiones
    decision = input('Deseas probaro otra vez? ')
    decision = decision.lower
    if decision == 'si':
        break
#Nuevo llamado a la función 

    else:
        adivinar()
        '''
import random 
def juego():
    numero=random.choice(range(1,100))
    intentos=0
    print("!!Welcome!!\n")
    nom=input("What´s your name? ")
    print("Guess the number i´m think\n")
    while True:
        intentos+=1
        print('Choise a  number that i think => ')
        eleccion = input()
        try:
            eleccion = int(eleccion)
        except:
            print('Not is a number')
            continue
        if numero==eleccion:
            print(f'This is amazing {nom} your win!!')
            break
        if numero>eleccion:
            print("The number is eldery")
        elif numero<eleccion:
            print("The number is low,")
        if intentos==5:
            print("Lose")
            break
    
juego()

        
        
