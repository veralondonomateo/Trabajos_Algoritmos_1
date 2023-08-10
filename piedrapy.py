import random 
print('Bienvenido')
computer_wins = 0
user_wins = 0
option = ('piedra', ' papel' , 'tijera')
rounds = 1
while True:
    print('*' * 10)
    print('ROUND' , rounds)
    print('*' * 10)
    print('user wins', user_wins)
    print('computer wins', computer_wins)   
    rounds += 1
    user_election = input('Elige piedra, papel o tijera =>')
    computer_election = random.choice(option)
    user_election = user_election.lower()
    if not user_election in option:
        print('Esa opción no es valida')

    if user_election == computer_election:
        print('Empate')
        continue
    elif user_election == 'piedra':
        if computer_election == ' papel':
            print(f'Perdiste, tu elegiste {user_election} y la computadora eligio {computer_election}')
            computer_wins += 1
        elif computer_election == 'tijera':
            print(f'Ganaste, tu elegiste {user_election} y la computadora eligio {computer_election}')    
            user_wins += 1
    elif user_election == 'papel':
        if computer_election == 'piedra':
            print(f'Ganaste, tu elegiste {user_election} y la computadora eligio {computer_election}') 
            user_wins += 1 
        elif computer_election == ' tijera':
            print(f'Perdiste, tu elegiste {user_election} y la computadora eligio {computer_election}')  
            computer_wins += 1
    elif user_election == 'tijera':
        if computer_election == 'piedra':
            print(f'Perdiste, tu elegiste {user_election} y la computadora eligio {computer_election}')  
            computer_wins += 1
        elif computer_election == 'papel':
            print(f'Ganaste, tu elegiste {user_election} y la computadora eligio {computer_election}')  
            user_wins += 1
    if user_wins == 3:
        print('¡ERES EL GANADOR ABSOLUTO!')
        break
    elif computer_wins == 3:
        print('¡LA PC GANO!')
        break
