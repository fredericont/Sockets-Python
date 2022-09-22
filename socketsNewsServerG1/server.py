#! /bin/python3 

import socket, threading
import datetime
from constantsServer import *
from constantsFeedparser import *

COR_TEXTO_1 = '\033[91m' # Vermelho
COR_TEXTO_2 = '\033[92m' # Verde
COR_TEXTO_3 = '\033[93m' # Amarelo
COR_TEXTO_4 = '\033[94m' # Azul 
COR_PADRAO  = '\033[0m'  # Reseta a cor

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORTA))
srv.listen()

def aceitandoCliente(conexao, endereco):

    while True: 
        
        date = datetime.datetime.now()
        datestr = date.strftime('%Y-%m-%d %H:%M:%S')           
        msg_recebida = conexao.recv(2048).decode(FORMAT)
        if not msg_recebida: break
        print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {msg_recebida}' + COR_PADRAO)
    
        if msg_recebida.lower() == '/c':
            conexao.send(bytes(CATEGORIAS, FORMAT))
            cat_recebida = conexao.recv(2048).decode(FORMAT)

            if cat_recebida.lower() == '/br':
                conexao.send(bytes("\n" + brTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)
            
            elif cat_recebida.lower() == '/car':
                conexao.send(bytes("\n" + carTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/cs':
                conexao.send(bytes("\n" + csTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/ce':
                conexao.send(bytes("\n" + ceTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/e':
                conexao.send(bytes("\n" + eTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)  

            elif cat_recebida.lower() == '/edu':
                conexao.send(bytes("\n" + eduTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/loto':
                conexao.send(bytes("\n" + lotoTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/mundo':
                conexao.send(bytes("\n" + mundoTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/m':
                conexao.send(bytes("\n" + mTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/nat':
                conexao.send(bytes("\n" + natTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/p':
                conexao.send(bytes("\n" + pTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/pop':
                conexao.send(bytes("\n" + popTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/tech':
                conexao.send(bytes("\n" + techTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)

            elif cat_recebida.lower() == '/tur':
                conexao.send(bytes("\n" + turTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {cat_recebida}' + COR_PADRAO)
                
        elif msg_recebida.lower() == '/reg':
            conexao.send(bytes(REGIAO, FORMAT))
            reg_recebida = conexao.recv(2048).decode(FORMAT)

            if reg_recebida.lower() == '/ac':
                conexao.send(bytes('\n' + acTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/al':
                conexao.send(bytes('\n' + alTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/ap':
                conexao.send(bytes('\n' + apTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/am':
                conexao.send(bytes('\n' + amTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/ba':
                conexao.send(bytes('\n' + baTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/ce':
                conexao.send(bytes('\n' + ceTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/df':
                conexao.send(bytes('\n' + dfTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/es':
                conexao.send(bytes('\n' + esTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/go':
                conexao.send(bytes('\n' + goTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/ma':
                conexao.send(bytes('\n' + maTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/mt':
                conexao.send(bytes('\n' + mtTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/ms':
                conexao.send(bytes('\n' + msTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/mg':
                conexao.send(bytes('\n' + mgTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/pa':
                conexao.send(bytes('\n' + paTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/pb':
                conexao.send(bytes('\n' + pbTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/pr':
                conexao.send(bytes('\n' + prTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/pe':
                conexao.send(bytes('\n' + peTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/rj':
                conexao.send(bytes('\n' + rjTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/rn':
                conexao.send(bytes('\n' + rnTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/rs':
                conexao.send(bytes('\n' + rsTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/ro':
                conexao.send(bytes('\n' + roTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/rr':
                conexao.send(bytes('\n' + rrTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/sc':
                conexao.send(bytes('\n' + scTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/sp':
                conexao.send(bytes('\n' + spTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/se':
                conexao.send(bytes('\n' + seTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

            elif reg_recebida.lower() == '/to':
                conexao.send(bytes('\n' + toTrat, FORMAT))
                print(datestr + " " + COR_TEXTO_2 + f'{endereco}: {reg_recebida}' + COR_PADRAO)

        elif msg_recebida.lower() == '/q':
            print(datestr + " " + COR_TEXTO_1 + f'{endereco}: Encerrou a conexão ' + COR_PADRAO)

        elif msg_recebida.lower() == '/help':
            conexao.send(bytes(HELP, FORMAT))
        
        else:
            print(datestr + " " + COR_TEXTO_1 + '[UNKNOWN COMMAND]' + COR_PADRAO)

def iniciandoConexao():
    while True:
        date = datetime.datetime.now()
        datestr = date.strftime('%Y-%m-%d %H:%M:%S')   
        try:
            print(COR_TEXTO_1 + '[LISTENING...]' + COR_PADRAO)
            conexao, endereco = srv.accept()
            print(f'\n[ESTABLISHED WITH  | {datestr} ] - {endereco [0]} : {endereco [1]}\n')           
            
            thread1 = threading.Thread(target=aceitandoCliente, args=(conexao, endereco))
            thread1.start()

            conexao.send(bytes(INICIAL, FORMAT))   

        except Exception as x:
            print(COR_TEXTO_3 + f'\nNão foi possível estabelecer a conexão.\n\nMotivo: {x} ' + COR_PADRAO)

iniciandoConexao()