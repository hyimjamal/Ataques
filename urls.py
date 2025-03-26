import json
import requests
import threading
import webbrowser
import sys
import time
from queue import Queue
from colorama import Fore, Style, init

# Inicializar Colorama
init(autoreset=True)

# Criar a fila globalmente antes de usar
urls = Queue()

def verificar_url():
    """Verifica se as URLs estão ativas e imprime o resultado"""
    while not urls.empty():
        url = urls.get()
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Encontrado: {url}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"[-] Não encontrado: {url}" + Style.RESET_ALL)
        except requests.exceptions.RequestException:
            print(Fore.YELLOW + f"[!] Erro ao acessar: {url}" + Style.RESET_ALL)
        urls.task_done()

def buscar_usuarios():
    """Coleta o nome do alvo e gera URLs de perfis em redes sociais"""
    usuario = input("Nome do alvo: ")

    # Lista de sites para busca
    sites = [
        f"https://facebook.com/{usuario}",
        f"https://youtube.com/{usuario}",
        f"https://instagram.com/{usuario}",
        f"https://twitter.com/{usuario}",
        f"https://linkedin.com/in/{usuario}",
        f"https://tiktok.com/@{usuario}",
        f"https://pinterest.com/{usuario}",
        f"https://snapchat.com/add/{usuario}",
        f"https://reddit.com/user/{usuario}",
        f"https://github.com/{usuario}",
        f"https://xvideos.com/{usuario}",
        f"https://pornhub.com/{usuario}",
        f"https://x.com/{usuario}",
        f"https://premierbet.com/{usuario}",
        f"https://elephantbet.com/{usuario}",
        f"https://sigeur.ac.mz/{usuario}",
        f"https://http://umb.ac.mz/eesiga/{usuario}",
        f"https://https://seul.unilurio.ac.mz/{usuario}",
        f"https://https://prereg.uem.mz/{usuario}",
        f"https://esura.ucm.ac.mz/{usuario}"
    ]

    for site in sites:
        urls.put(site)

    threads = []
    for _ in range(5):  # Criar 5 threads para processar as URLs
        thread = threading.Thread(target=verificar_url)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Fore.RED + "Procurando por arquivos online....")
    time.sleep(2)
    print("*" * 100)
    
    return usuario, sites  # Retorna dados para salvar no JSON

def buscar_arquivos_online(usuario):
    """Gera dorks do Google para buscar arquivos relacionados ao alvo"""
    dorks = [
        f'site:.mz (filetype:pdf OR filetype:docx OR filetype:txt OR filetype:xlsx OR filetype:pptx) intext:"{usuario}"'
    ]

    for dork in dorks:
        url = f"https://www.google.com/search?q={dork}"
        print(f"{Fore.GREEN} Encontrado:\n {url}")
        
        permissao = input("Deseja abrir o navegador para verificar? [S/N]: ").upper()
        if permissao == 'S':
            webbrowser.open(url)
        elif permissao != 'N':
            print("Comando incorreto, fechando.")
            sys.exit()
    
    return dorks  # Retorna os dorks para salvar no JSON

if __name__ == "__main__":
    usuario, contas = buscar_usuarios()
    dorks = buscar_arquivos_online(usuario)

    # Salvar os resultados em um arquivo JSON
    dados = {"Usuario": usuario, "Perfis Encontrados": contas, "Dorks de Busca": dorks}
    with open("data.json", "w") as thefile:
        json.dump(dados, thefile, indent=4)

    print(Fore.CYAN + "\nOs resultados foram salvos em 'data.json'!")
