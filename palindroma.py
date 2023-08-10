if __name__ == '__main__':

    print('*' * 10)
    print('DESCUBRE SI UNA PALABRA ES PALINDROMA')
    print('*' * 10)

    def palindroma():
        election = input('Ingresa la palabra => ')
        rev = election[::-1]
        if rev == election:
            print(f'{election} es palindrome')
        else:
            print(f'{election} no es palindrome')

    palindroma()

    while True:
        print('*' * 10 )
        final_election = input('Deseas intentar con otra palabra? ').lower()
        if final_election == 'si':
            palindroma()
        else:
            break