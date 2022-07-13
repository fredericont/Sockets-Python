#! /bin/python3 

import os, sys, socket

HOST = ''
PORTA = 65000
DIR_PATH = '/home/fred/Sockets/Servidor/arquivos_servidor'
LIST_ARQ = os.listdir(DIR_PATH)
ENCER_CON = ('\nConexão com o servidor encerrada. Até a próxima!\n')
MENU = ('\nLISTA DE COMANDOS ↴\n \
         \n  \\f ⇾ Listar arquivos \
         \n  \\d:(arquivo) ⇾ Baixar arquivo \
         \n  \\u:(arquivo) ⇾ Upload de arquivo  \
         \n  \\q ⇾ Sair\n\n')
MSG_INICIAL = ('\n Digite um comando (\\h para listar os comandos possíveis):\n ')
NOT_FOUND = ('\nArquivo não encontrado')
FORMAT = 'utf-8'

arquivos = []
for f in LIST_ARQ:
    f_path = os.path.join(DIR_PATH,f)
    f_size = os.path.getsize(f_path)
    F_SIZE_STR = str(f_size)
    FILE_WITH_SIZE = f'{f} ({F_SIZE_STR} bytes)'
    arquivos.append(FILE_WITH_SIZE)

LIST_STR = ('\n'.join(map(str, arquivos)))

while True:
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((HOST, PORTA))
    srv.listen()
    print('Aguardando conexões...')

    conexao, endereco = srv.accept()
    print(f'Conexão estabelecida - {endereco [0]} : {endereco [1]}')
    conexao.send(bytes(MSG_INICIAL, 'utf-8'))
    
    while True:
        msg_recebida = conexao.recv(2048).decode(FORMAT)
        
        if msg_recebida.lower() == '\\f': 
            print(endereco, ' Solicitou lista de arquivos ')
            conexao.send(bytes('\nLISTA DE ARQUIVOS ↴\n' + LIST_STR + " ", FORMAT))
            print('Enviado ✓')
        
        elif msg_recebida[:3].lower() == '\\d:':
            os.chdir('/home/fred/Sockets/Servidor/arquivos_servidor')
            ONLY_NAME = msg_recebida[3:]
            print(endereco, f'Solicitou o envio do arquivo {ONLY_NAME}')
            
            with open(ONLY_NAME, 'rb') as arquivo: 
                ARQ_ENV = arquivo.read()
                conexao.send(ARQ_ENV)
                print('Enviado ✓')

        elif msg_recebida.lower() == '\\h':
            print(endereco, 'Solicitou lista de comandos')
            conexao.send(bytes(MENU, FORMAT))
            print('Enviado ✓')

        elif msg_recebida.lower() == '\\q':
            print(f'\nEncerrando conexão com o IP {endereco [0]} na porta {endereco [1]}\n')
            conexao.send(bytes(ENCER_CON, FORMAT))
            conexao.close()
            break
        
        else:
            continue
