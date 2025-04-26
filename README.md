# Bot de CS da FURIA
Este é um bot do Telegram desenvolvido em Python que fornece informações sobre o time de CS:GO da FURIA. Com ele, os usuários podem acessar dados sobre jogadores, calendário de campeonatos, histórico de desempenho e curiosidades da equipe. Fiz o bot pensando em coisas qbásicas que eu mesmo queria saber, já que não sei muito sobre o time de CS da FURIA.

## Tecnologias utilizadas
Basicamente o que foi utilizado aqui foi python e pyTelegramBotApi que pode ser instalado via:
```shell
pip install pyTelegramBotAPI
```

## Comandos principais
/start: Inicia a conversa com o bot e apresenta as opções disponíveis.

/time_e_jogadores: Exibe informações sobre o time e seus jogadores.

/calendario: Mostra os próximos campeonatos e compromissos.

/historico: Informa o desempenho e histórico da equipe.

/curiosidades: Traz curiosidades aleatórias sobre o time.

Além dessas, também existem subcomandos em cada uma dessas funcionalidades (exceto /curiosidades) que vão segtuindo o fluxo da aplicação. Em /curiosidades é ativada uma curiosidade aleatória sobre o time. O comando inicial deve sempre ser o /start e não é possível pular comandos que não estejam no mesmo fluxo, exemplo: caso tenha utilizado o comando /historico, não será possível logo em seguida usar o comando /time_e_jogadores, para isso será necessário voltar para o /start e depois usar o comando /time_e_jogadores

Segue uma lista com os subcomandos existentes para cada comando principal:

1. /time_e_jogadores

* /capitao - retorna o capitão atual do time
* /treinador - retorna os treinadores atuais do elenco
* /jogadores - retorna os jogadores principais do elenco atual

2. /historico

* /criacao - fala um pouco sobre a criação do time de CS da FURIA
* /ultimos_tecnicos - retorna os ultimos técnicos do time
* /ultimos_jogadores - retorna os 5 últimos jogadores do time
* /competicoes - retorna uma lista com todas as competições já ganhas pelo time

3. /calendarios

* /campeonatos - retorna os próximos campeonatos que om time tem confirmado para jogar (no momento não encontrei nenhum)
* /resultados - resultados dos últimos 5 jogos do time

## Pastas e modularização

Nesse projeto existem duas pastas principais que são elas:

1. /handlers

* Nela estão contidos os arquivos com cada handler para os comandos, cada arquivo dentro da pasta contém um arquivo responsável por lidar com um comando principal e seus subcomandos

2. /utils

* Aqui contém dois arquivos, onde um deles é o state.py que contém as funções e variáveis que armazenam o último comando e último subcomando utilizado pelo usuário. O outro arquivo é o middleware_bot.py que utiliza dessas variáveis para filtrar os fluxos de comando, impedindo que subcomandos de um comando principal sejam utilizados dentro de outro comando principal. O middleware é responsável pelo gerenciamento dos fluxos do bot.

3. Raiz do projeto

* Aqui basicamente tem o código principal para rodar que está em bot.py, ele é onde mora o bot que é utilizado em toda a aplicação

## Estrutura do Projeto

```shell
├── handlers/
│   ├── time_e_jogadores.py
│   ├── calendarios.py
│   ├── historico.py
│   └── curiosidades.py
├── utils/
│   ├── middleware_bot.py
│   └── state.py
├── .env
├── bot.py
└── README.md
```

## Fontes utilizadas para fazer o projeto

https://www.esportelandia.com.br/esports/furia-esports-historia/

https://escharts.com/pt/teams/csgo/furia

https://www.hltv.org/stats/players/15631/kscerato