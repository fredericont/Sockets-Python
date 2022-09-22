HOST = ''
PORTA = 65000
FORMAT = 'utf-8'
INICIAL = '-'*53 + '\nSeja bem vinda(o) ao servidor de notícias em Python!\n' + '-'*53 + '\nA partir das consultas fornecidas, terás acesso as 10 principais notícias do dia referentes aos temas selecionados.' + '\n\nPor gentileza, informe o modo conforme gostaria de ler as noticias, entre as possibilidades abaixo:\n\n- Para notícias subdivididas por categorias, digite /c \n- Para noticias da sua região, digite /reg\n\n'

CATEGORIAS = '\n' + '-'*54 + '\nSelecione uma categoria abaixo, conforme o seu código:\n' + '-'*54 + '\n\nNoticias do Brasil    ➜    /br' + \
    '\nCarros                ➜    /car'  \
        '\nCiência e Saúde       ➜    /cs'  \
            '\nConcuros e empregos   ➜    /ce'  \
                '\nEconomia              ➜    /e'  \
                    '\nEducação              ➜    /edu'  \
                        '\nLoterias              ➜    /loto'  \
                            '\nNotícias do Mundo     ➜    /mundo'  \
                                '\nMusica                ➜    /m'  \
                                    '\nNatureza              ➜    /nat'  \
                                        '\nPolítica              ➜    /p'  \
                                            '\nPop e Arte            ➜    /pop'  \
                                                '\nTecnologia e Games    ➜    /tech' \
                                                    '\nTurismo e Viagens     ➜    /tur'


REGIAO = '\n' + '-'*60 + '\nPor gentileza, insira o estado conforme o respectivo código\n' + '-'*60 +\
    '\nAcre                     ➜   /ac'+\
        '\nAlagoas                  ➜   /al'+\
            '\nAmapá                    ➜   /ap'+\
                '\nAmazonas                 ➜   /am'+\
                    '\nBahia                    ➜   /ba'+\
                        '\nCeará                    ➜   /ce'+\
                            '\nDistrito Federal         ➜   /df'+\
                                '\nEspírito Santo           ➜   /es'+\
                                    '\nGoiás                    ➜   /go'+\
                                        '\nMaranhão                 ➜   /ma'+\
                                            '\nMato Grosso              ➜   /mt'+\
                                                '\nMato Grosso do Sul       ➜   /ms'+\
                                                    '\nMinas Gerais             ➜   /mg'+\
                                                        '\nPará                     ➜   /pa'+\
                                                            '\nParaíba                  ➜   /pb'+\
                                                                '\nParaná                   ➜   /pr'+\
                                                                    '\nPernambuco               ➜   /pe'+\
                                                                        '\nRio de Janeiro           ➜   /rj'+\
                                                                            '\nRio Grande do Norte      ➜   /rn'+\
                                                                                '\nRondônia                 ➜   /ro'+\
                                                                                    '\nRorâima                  ➜   /rr'+\
                                                                                        '\nSanta Catarina           ➜   /sc'+\
                                                                                            '\nSão Paulo                ➜   /sp'+\
                                                                                                '\nSergipe                  ➜   /se'+\
                                                                                                    '\nTocantins                ➜   /to'

HELP = '\n[COMANDOS POSSÍVEIS]:\n- /c    ➜ Leitura de notícias subdivididas em categorias\n- /reg  ➜ Leitura de notícias subdivididas por estado\n- /q    ➜ Encerrar conexão com servidor\n'
