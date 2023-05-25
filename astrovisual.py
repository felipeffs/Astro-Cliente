import requests


def login():
    print(f'====LOGAR====')
    user = input(f'Login: ')
    password = input(f'Password: ')


def make_a_request():
    user_id = int(input("id do usuário: "))
    req = requests.get(f"http://localhost:5136/api/ZodiacProfiles/{user_id}").json()
    print(f'Nome: {req["name"]}')
    print(f'Sobre Mim: {req["description"]}')
    print(f'Signo: {req["signName"]}')

    sign_data = req["signData"]
    print(f'Cor do Dia: {sign_data["colorDay"]}')
    print(f'Bebida do Dia: {sign_data["drink"]}')
    print(f'Número da Sorte: {sign_data["number"]}')


class AstroVisual:
    if __name__ == '__main__':
        make_a_request()
        # login()
