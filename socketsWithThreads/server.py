#! /bin/python3 
import os, threading, socket, time, sys
from constants import *

try:
    if sys.argv[1] == '/start':
        pass
    elif sys.argv[1] == '/help':
        print('\nArgumentos disponíveis ➝ ./nome_do_arquivo.py < /start | /help >\n ')
        exit()
    else:
        print('\nPor gentileza, insira o seguinte comando ➝ ./nome_da_arquivo.py /help\n ')
        exit()
except IndexError:
        print('\nErro inesperado. Por favor, insira ➝ ./nome_da_arquivo.py /help\n ')
        exit()

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORTA))
srv.listen()

def aceitandoCliente(conexao, endereco):
    while True:
        msg_recebida = conexao.recv(2048).decode(FORMAT)
        if not msg_recebida: break
        print(f'\n{endereco} : {msg_recebida}')

        try:
            if msg_recebida.lower() == '\\f': 
                print(endereco, ' Solicitou lista de arquivos ')
                log_f = (f'({DATE} | {endereco [0]} : {endereco [1]}) - {msg_recebida}')
                LOG_LIST.append(str(log_f))
                conexao.send(bytes('\nLISTA DE ARQUIVOS ↴\n' + LIST_STR + " ", FORMAT))
                time.sleep(0.5)
                print('Enviado ✓\n')
            
            elif msg_recebida[:3].lower() == '\\d:':
                os.chdir(DIR_PATH)
                log_d = (f'({DATE} | {endereco [0]} : {endereco [1]}) - {msg_recebida}')
                LOG_LIST.append(str(log_d))
                ONLY_NAME = msg_recebida[3:]
                print(endereco, f'Solicitou o envio do arquivo {ONLY_NAME}')
                
                with open(DIR_PATH + ONLY_NAME, 'rb') as READ_D:
                    OPEN_D = READ_D.read()
                    conexao.send(OPEN_D)
                
            elif msg_recebida[:3].lower() == '\\u:':
                os.chdir(DIR_PATH)
                ONLY_NAME_UP = msg_recebida[3:]
                log_u = (f'({DATE} | {endereco [0]} : {endereco [1]}) - {msg_recebida}')
                LOG_LIST.append(str(log_u))
                UP_CLIENTE = conexao.recv(1024)

                with open(DIR_PATH + ONLY_NAME_UP, 'wb') as arquivo_up:
                    while (UP_CLIENTE):
                        arquivo_up.write(UP_CLIENTE)
                        UP_CLIENTE = conexao.recv(1024)
                        
                    print(endereco, f'Realizou o envio do arquivo {ONLY_NAME}')
                
            elif msg_recebida.lower() == '\\h':
                print(endereco, 'Solicitou lista de comandos')
                log_h = (f'({DATE} | {endereco [0]} : {endereco [1]}) - {msg_recebida}')
                LOG_LIST.append(str(log_h))
                conexao.send(bytes(MENU, FORMAT))
                time.sleep(0.5)
                print('Enviado ✓\n')

            elif msg_recebida.lower() == '\\q':
                print(f'\nEncerrando conexão com o IP {endereco [0]} na porta {endereco [1]}\n')
                log_q = (f'({DATE} | {endereco [0]} : {endereco [1]}) - {msg_recebida}')
                LOG_LIST.append(log_q)            
                conexao.send(bytes(ENCER_CON, FORMAT))
                break

            elif msg_recebida.lower() == '\\m':
                print(endereco, 'Solicitou arquivo de logs')
                log_m = (f'({DATE} | {endereco [0]} : {endereco [1]}) - {msg_recebida}')
                LOG_LIST.append(log_m)
                LOG_STR = ('\n'.join(map(str, LOG_LIST)))
                conexao.send(bytes('\nLOGS ↴\n' + LOG_STR + " ", FORMAT))
                time.sleep(0.5)
                print('Enviado ✓\n')      
        except:
            print('\nComando não encontrado. Por favor, digite um comando válido.\n')
            continue


def iniciandoConexao():
    while True:
        try:
            print('Aguardando conexões...')
            conexao, endereco = srv.accept()
            print(f'Conexão estabelecida - {endereco [0]} : {endereco [1]}')
            thread1 = threading.Thread(target=aceitandoCliente, args=(conexao, endereco))
            thread1.start()
        
        except Exception as x:
            print(f'\nNão foi possível estabelecer a conexão.\n\nERRO: {x} ')

iniciandoConexao()
