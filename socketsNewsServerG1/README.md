Sobre o programa:
- O servidor de notícias com base nos artigos em RSS disponibilizados pelo G1, é uma forma didática de se trabalhar com a biblioteca feedparser. No programa, busquei trazer de maneira simples, tornando o código até mesmo não otimizado, contudo de fácil compreensão para quem está estudando. 

Para sua utilização, é necessário que haja a biblioteca Feedparser instalada. Caso não haja, segue o comando abaixo:
	$ pip install feedparser

Assim que instaladobasta que os arquivos server.py / constantsServer.py / constantsFeedparser.py estejam nos mesmos diretórios. Assim como o client.py precisa estar no mesmo diretório que as suas constantes. 

Para execução do programa apenas com um ./ habilite as permissões de leitura, escrita e execução para o usuário que irá utilizar. Geralmente realizo o procediemnto abaixo:

chmod 777 server.py
chmod 777 client.py

Assim, quando ajustadas as permissões de arquivo, para execução de ambos programas basta em seu terminar executar:

./server.py
./cliente.py

Quando executado o arquivo server, aguarde em terminal aparecer [LISTENING...] em vermelho. Isso implica que o servidor está ouvindo na porta o qual foi definido.
Obs: Desde que inserir em função a inicialização do servidor, percebi que tem levado alguns segundos para o mesmo 'subir' e ficar ouvindo na porta 65000. Em futuras versões buscarei optimizar. 

Assim, com o servidor ouvindo, basta executar o programa client.py. 

Funcionalidades do servidor:
- Com o servidor em execução poderás ler noticias subdividos por categorias ou filtrando pelo estado. Para iso os comandos /c e /reg o encaminhará para o modo com que gostaria de ler as noticias.

Considerações finais:
- Este programa foi desenvolvido com o intuito de aperfeiçoar algumas skills acerca da utilização da biblioteca. Versões mais otimizadas virão futuramente. 
