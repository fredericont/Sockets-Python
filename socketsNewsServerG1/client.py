#! /bin/python3 

import datetime
from constantsClient import*

COR_TEXTO_1 = '\033[91m' # Vermelho
COR_TEXTO_2 = '\033[92m' # Verde
COR_TEXTO_3 = '\033[93m' # Amarelo
COR_PADRAO  = '\033[0m'  # Reseta Color

# Horário


try:
    date = datetime.datetime.now()   
    datestr = date.strftime('%Y-%m-%d %H:%M:%S')
    client.connect((HOST, PORTA))
    print(COR_TEXTO_1 + '\n[CONEXÃO ESTABELECIDA]' + " | " + datestr + '\n' + COR_PADRAO )

    MSG_INICIAL = client.recv(BUFFER)
    print(MSG_INICIAL.decode(FORMAT))

    while True:
      date = datetime.datetime.now()   
      datestr = date.strftime('%Y-%m-%d %H:%M:%S')
      
      cmd_interacao = input('\n\n[DIGITE UM COMANDO]  |  [/help]\n↳ ')
      client.send(cmd_interacao.encode(FORMAT))

      if cmd_interacao.lower() == '/c':
         cat_recebidas = client.recv(BUFFER)
         print(cat_recebidas.decode(FORMAT))

         cat_enviada = input('\nInforme a categoria no qual gostaria de receber notícias: ')
         client.send(cat_enviada.encode(FORMAT))
         
         if cat_enviada.lower() == '/br':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))
      
         elif cat_enviada.lower() == '/car':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/cs':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/ce':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/e':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/edu':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))        
      
         elif cat_enviada.lower() == '/loto':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))        
      
         elif cat_enviada.lower() == '/mundo':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/m':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/nat':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/p':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/pop':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/tech':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif cat_enviada.lower() == '/tur':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))
         
         else:
            print('\nCOMANDO INVÁLIDO')
      
      elif cmd_interacao.lower() == '/reg':
         reg_recebidas = client.recv(BUFFER)
         print(reg_recebidas.decode(FORMAT))

         reg_enviada = input('\nInforme o estado no qual gostaria de ler as principais notícias: ')
         client.send(reg_enviada.encode(FORMAT))

         if reg_enviada.lower() == '/ac':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/al':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/ap':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/am':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/ba':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/ce':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/df':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/es':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/go':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))
         
         elif reg_enviada.lower() == '/ma':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/mt':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/ms':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/mg':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/pa':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))
         
         elif reg_enviada.lower() == '/pb':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/pr':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/pe':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/rj':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/rn':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/rs':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/ro':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/rr':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/sc':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/sp':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/se':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         elif reg_enviada.lower() == '/to':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

         else:
            print(COR_TEXTO_1 + f'\n[ESTADO NÃO ENCONTRADO. POR FAVOR, INSIRA UM ESTADO VÁLIDO]\n' + COR_PADRAO + COR_TEXTO_2 + f'Consulta realizada: {reg_enviada}\n' + COR_PADRAO)

      elif cmd_interacao.lower() == '/q':
         print(COR_TEXTO_1 + '\n[CLOSING CONNECTION...]' + " | " + datestr + COR_PADRAO + "\n")
         break

      elif cmd_interacao.lower() == '/help':
            recebido = client.recv(BUFFER)
            print(recebido.decode(FORMAT))

      else:
         print(COR_TEXTO_1 + '\n[COMANDO INVÁLIDO - /help]' + COR_PADRAO)
 
except Exception as y:
    print(f'\n\nNão foi possível conexão.\nMotivo: {y}\n\n')