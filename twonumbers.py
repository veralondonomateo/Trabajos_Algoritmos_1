print('TWO NUMBERS CALCULATOR')
def twonumbers():
    #Elección de los números
    electionone = int(input('Choise a number => '))
    electiontwo = int(input('Choise a other number =>'))

    def operation():

        print('What operation you wnat make?')
        print('1- SUMAR')
        print('2- RESTAR')
        print('3- MUTIPLICAR')
        print('4- DIVIDIR')

        election_operation = int(input())

        if election_operation == 1:
            result = electionone + electiontwo
            print(result)
        elif election_operation == 2:
            result = electionone - electiontwo
            print(result)
        elif election_operation == 3:
            result = electionone * electiontwo
            print(result)
        elif election_operation == 4:
            result = electionone / electiontwo
            print(result)
        else:
            result = 'Don´t exist this option'
            print(result)
        
        
    
    
    resultone = operation()
    return resultone
   


twonumbers()

while True:
   
    print('1- You want make with other numbers? ')
    print('2- You want change of operation? ')
    print('3- You want EXIT')
    final_option = input()

    if final_option == 1 :
            twonumbers()

    elif final_option == 2:
            twonumbers()
    