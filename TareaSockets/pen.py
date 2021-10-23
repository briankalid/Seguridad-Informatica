import requests



#  From itertools
def ingres(*args, repeat=4, username = None):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[str(y)] for x in result for y in pool]

    for prod in result:
        pswd = ''.join(prod)
        r = requests.request(method='get', url = 'http://localhost:8000/user/', data = {'name': username,'pswd': pswd})
        if r.status_code == 404:
            return "Usuario no encontrado"
        
        elif r.status_code == 200:
            return 'Contrasena encontrada: '+pswd

    return 'Contrasena no encontrada'





def create(username, pswd):
    r = requests.request(method='post', url='http://localhost:8000/user/', data={'name':username, 'pswd': pswd})
    print(r.text)

if __name__ == '__main__':

    while True:
        print('Para crear usuario presione 1, para adivinar la contrasena presione 2')

        select = input()

        if select == '1':
            username = input('Nombre de usuario(maximo 60 caracteres): ')
            pswd = input('contrasena(solo 4 numeros): ')
            create(username, pswd)        

        elif select == '2':
            username = input('Nombre de usuario: ')
            print(ingres(range(10), username=username))

        else:
            print('opcion invalida!')

