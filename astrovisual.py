import requests
import os


def astro_visual():
    print(f"{'Astro':=^53}")
    username = str(input("Nome de Usuário: "))
    password = str(input("Senha: "))

    print(f'=' * 55)

    try:
        req = requests.get(f"http://localhost:5136/api/ZodiacProfiles/Login/{username}/{password}")
    except requests.exceptions.RequestException as e:
        print("Servidor fora do ar")
        return
    else:
        if req.status_code != 200:
            print(f"Usuário ou Senha incorreto")
            return
        userdata = req.json()

    os.system('cls')
    print(f"{'Astro':=^55}")
    print(f'Nome: {userdata["name"]}')
    print(f'Sobre Mim: {userdata["description"]}')
    print(f'Signo: {userdata["signName"]}')

    sign_data = userdata["signData"]

    print(f'Elemento: {sign_data["element"]}')
    print(f'Cor do Dia: {sign_data["colorDay"]}')
    print(f'Número da Sorte: {sign_data["number"]}')
    print(f'Flor: {sign_data["flower"]}')

    if userdata["membership"]:
        print(f'Bebida do Dia: {sign_data["drink"]}')
        print(f'Sorte no Amor: {sign_data["love"]}')


class AstroVisual:
    if __name__ == '__main__':
        astro_visual()
        input()
