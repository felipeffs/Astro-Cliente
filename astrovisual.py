import requests
import os

# Colors
default = "\033[0;0m"
gold = "\033[0;33m"
red = "\033[0;31m"


def astro_visual():
    print(f"{'Astro':=^55}")
    username = str(input("Nome de Usuário: "))
    password = str(input("Senha: "))

    print(f'=' * 55)

    try:
        req = requests.get(f"http://localhost:5136/api/ZodiacProfiles/Login/{username}/{password}")
    except requests.exceptions.RequestException:
        print(f"{red}Erro: Servidor fora do ar{default}")
        return False
    else:
        if req.status_code != 200:
            print(f"{red}Erro: Usuário ou Senha incorreto{default}")
            return False
        userdata = req.json()

    os.system('cls')
    print(f"{'Astro Profile':=^55}")
    print(f'Nome: {userdata["name"]}')
    print(f'Sobre Mim: {userdata["description"]}')
    print(f'Signo: {userdata["signName"]}')
    print(f'Plano: { f"{gold}Premium{default}" if  userdata["membership"] else "Gratuito"}')

    print(f"{'Informações do Signo':=^55}")
    sign_data = userdata["signData"]

    print(f'Elemento: {sign_data["element"]}')
    print(f'Cor do Dia: {sign_data["colorDay"]}')
    print(f'Número da Sorte: {sign_data["number"]}')
    print(f'Flor: {sign_data["flower"]}')

    if userdata["membership"]:
        print(f'{gold}Bebida do Dia: {sign_data["drink"]}')
        print(f'Sorte no Amor: {sign_data["love"]}{default}')

    return True


class AstroVisual:
    if __name__ == '__main__':
        while True:
            if not astro_visual():
                logoff_input = input(f"{'[1] Tentar Novamente'}{'[Qualquer Tecla] Sair':>35}\n")
                os.system('cls')
                if logoff_input == '1':
                    continue
                else:
                    break
            else:
                print(f'=' * 55)
                logoff_input = input(f"{'[1] Deslogar'}{'[Qualquer Tecla] Sair':>43}\n")
                os.system('cls')
                if logoff_input == '1':
                    continue
                else:
                    break
