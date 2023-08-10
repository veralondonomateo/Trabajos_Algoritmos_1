import secrets

if __name__ == '__main__':
    names = ['Devin', 'Simon' ,'Julian','Saul', 'Andres', 'Juan Camilo','Manuela', 'Julieta','Henaito','Ricardo','Miguel' ]
    names_final = 3

    fivenames = secrets.SystemRandom().sample(names, names_final)
    for i in fivenames:
        print('Hola', i)
