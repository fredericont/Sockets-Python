import os, datetime

HOST = ''

PORTA = 65000

DIR_PATH = '/home/fred/Sockets/Servidor/arquivos_servidor/'

BUFFER = 100000

LIST_ARQ = os.listdir(DIR_PATH)

ENCER_CON = ('\nConexão com o servidor encerrada. Até a próxima!\n')

MENU = ('\nLISTA DE COMANDOS ↴\n \
         \n  \\f            ⇾    Listar arquivos \
         \n  \\m            ⇾    Verificar histórico \
         \n  \\d:arquivo    ⇾    Baixar arquivo \
         \n  \\u:arquivo    ⇾    Upload de arquivo  \
         \n  \\q            ⇾    Sair\n\n')

MSG_INICIAL = ('\nDigite um comando (\\h para listar os comandos possíveis):\n ')

NOT_FOUND = ('\nArquivo não encontrado')

FORMAT = 'utf-8'

DATE_NOW = datetime.datetime.now()

DATE_NOW_STR = DATE_NOW.strftime('%d/%m/%Y %H:%M')

DATE = datetime.datetime.strptime(DATE_NOW_STR, '%d/%m/%Y %H:%M')

arquivos = []

for f in LIST_ARQ:
    f_path = os.path.join(DIR_PATH,f)
    f_size = os.path.getsize(f_path)
    F_SIZE_STR = str(f_size)
    FILE_WITH_SIZE = f'{f} ({F_SIZE_STR} bytes)'
    arquivos.append(FILE_WITH_SIZE)

LIST_STR = ('\n'.join(map(str, arquivos)))

LOG_LIST = []
