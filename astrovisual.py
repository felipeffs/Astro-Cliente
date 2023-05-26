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
        return False
    else:
        if req.status_code != 200:
            print(f"Usuário ou Senha incorreto")
            return False
        userdata = req.json()

    os.system('cls')
    print(f"{'Astro':=^55}")
    print(f'Nome: {userdata["name"]}')
    print(f'Sobre Mim: {userdata["description"]}')
    print(f'Signo: {userdata["signName"]}')
    print(f'Membro: { "Premium" if  userdata["membership"] else "Free"}')

    sign_data = userdata["signData"]

    print(f'Elemento: {sign_data["element"]}')
    print(f'Cor do Dia: {sign_data["colorDay"]}')
    print(f'Número da Sorte: {sign_data["number"]}')
    print(f'Flor: {sign_data["flower"]}')

    if userdata["membership"]:
        print(f'Bebida do Dia: {sign_data["drink"]}')
        print(f'Sorte no Amor: {sign_data["love"]}')

    return True


class AstroVisual:
    if __name__ == '__main__':
        while True:
            if not astro_visual():
                logoff_input = input("Pressione 1 para tentar novamente ou 2 para sair\n")
                os.system('cls')
                if logoff_input == '1':
                    continue
                else:
                    break
                continue
            else:
                print(f'=' * 55)
                logoff_input = input("Pressione 1 para fazer logout ou 2 para sair\n")
                os.system('cls')
                if logoff_input == '1':
                    continue
                else:
                    break
