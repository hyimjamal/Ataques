import json
from colorama import init, Fore, Style
import time
import webbrowser
import sys
def Urls():
    usuario = input("Nome do alvo: ")
    
    # Lista de sites mais populares
    Contas = [
        Fore.GREEN+
        f"https://Facebook.com/{usuario}",
        f"https://Youtube.com/{usuario}",
        f"https://Instagram.com/{usuario}",
        f"https://Twitter.com/{usuario}",
        f"https://Linkedin.com/in/{usuario}",
        f"https://Tiktok.com/@{usuario}",
        f"https://Pinterest.com/{usuario}",
        f"https://Snapchat.com/add/{usuario}",
        f"https://Reddit.com/user/{usuario}",
        f"https://GitHub.com/{usuario}"
  ]
    
    # Exibe todas as URLs geradas
    print("Aqui estão suas contas com o nome de usuário fornecido:")
    for conta in Contas:
        print(conta)
    
    print(Fore.RED +"Procurando por arquivos online....")
    time.sleep(2)
    print("*"*100)
    dorks = [
        f'site:.mz (filetype:pdf OR filetype:docx OR filetype:txt OR filetype:xlsx OR filetype:pptx) intext:"{usuario}"'
    ]

    for dork in dorks:
        url = f"https://www.google.com/search?q={dork}"
        print(f"{Fore.GREEN} Encontrado:\n {url}")
        if True:
            permissao=input("Deseja abrir o  navegador pra dar uma olhada?[S] ou [N]").upper()
            if permissao=='S':
                webbrowser.open(url)
                continue
            elif permissao=='N':
                pass
            else:
                print("Comando Incorreto, Fechando")
                sys.exit()

# Exemplo de uso
if __name__=="__main__":
    Urls()
    dados = Contas,dorks
    json_string = json.dumps(dados)  # Converte dicionário para JSON (string)
    with open("data.json","w") as thefile:
        thefile.write(json_string)
