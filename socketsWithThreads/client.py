#! /bin/python3 

import socket, os, time

HOST = '127.0.0.1'
PORTA = 65000
FORMAT = 'utf-8'
BUFFER = 2048
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LOCAL = os.chdir('/home/fred/Sockets/Cliente/downloads/')

try:
    client.connect((HOST, PORTA))
    print(f'\nConexão estabelecida com o servidor\n')

    while True:
        cmd_interacao = input('\nDigite um comando\n↳ ')

        client.send(cmd_interacao.encode(FORMAT))

        if cmd_interacao == '\\q':
            RECEBE_INFO = client.recv(BUFFER)
            RECEBE_INFO_STR = RECEBE_INFO.decode(FORMAT)
            print('\nConexão encerrada')
            client.close()        
            break

        elif cmd_interacao == '\\h':
            RECEBE_INFO = client.recv(BUFFER)
            RECEBE_INFO_STR = RECEBE_INFO.decode(FORMAT)
            print(RECEBE_INFO_STR)

        elif cmd_interacao == '\\m':
            RECEBE_INFO = client.recv(BUFFER)
            RECEBE_INFO_STR = RECEBE_INFO.decode(FORMAT)
            print(RECEBE_INFO_STR)

        elif cmd_interacao == '\\f':
            RECEBE_INFO = client.recv(BUFFER)
            RECEBE_INFO_STR = RECEBE_INFO.decode(FORMAT)
            print(RECEBE_INFO_STR)

        elif cmd_interacao[:3].lower() == '\\d:':
            REAL_NAME = cmd_interacao[3:]
            os.chdir('/home/fred/Sockets/Cliente/downloads/')     
            
            with open('/home/fred/Sockets/Cliente/downloads/' + REAL_NAME, 'wb') as ARQUIVO_RECV:
                DADOS_RECV = client.recv(BUFFER)     
                while (DADOS_RECV):
                    ARQUIVO_RECV.write(DADOS_RECV)    
                    DADOS_RECV = client.recv(BUFFER)
                    time.sleep(0.3)
                    if not (DADOS_RECV):
                        continue

                       
        elif cmd_interacao[:3].lower() == '\\u:':
            os.chdir('/home/fred/Sockets/Cliente/downloads/')  
            REAL_NAME_UP = cmd_interacao[3:]
            
            with open('/home/fred/Sockets/Cliente/downloads/' + REAL_NAME_UP, 'rb') as ARQUIVO_CLI_UP:
                ARQ_ENV_UP = ARQUIVO_CLI_UP.read()
                client.send(ARQ_ENV_UP)
                print(f'\nRealizado o envio do arquivo {REAL_NAME_UP} para o servidor')             

except ConnectionRefusedError:
    print('\nServidor indisponível para conexão no momento\n')

except OSError:
    print('Contate o suporte\n') 




        



