import telebot
import textwrap
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

last_main_command = ""



@bot.message_handler(commands=["capitao"])
def leader(msg):
    if (last_main_command == "/time_e_jogadores"):
        reply = textwrap.dedent(f"""
        O capitão do time atualmente é o FalleN, responsável pelas estratégias e coordenação do time durante as partidas.
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)
        bot.reply_to(msg,reply)
        
@bot.message_handler(commands=["treinador"])
def leader(msg):
    if (last_main_command == "/time_e_jogadores"):
        reply = textwrap.dedent(f"""
        Atualmente os treinadores do time são Sidde (Sidnei Macedo) e Heppa (Juan Borges), responáveis por estudar adversários, criarem táticas, dar feedbacks aos seus jogadores e preparar a equipe fora do servidor.
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)
        bot.reply_to(msg, reply)


@bot.message_handler(commands=["jogadores"])
def players(msg):

    if (last_main_command == "/time_e_jogadores"):
        reply = textwrap.dedent(f"""
        Atualmente os jogadores do time titular de CS FURIA são:
        
        KSCERATO - Kaike Cerato (Brasil)
        Yuurih - Yuri Boian (Brasil)
        FalleN - Gabriel Toledo (Brasil)
        Molodoi - Danil Golubenko (Cazaquistão)
        YEKINDAR - Mareks Gaļinskis (Letônia)
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)

        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=["resultados"])
def last_games(msg):

    if (last_main_command == "/calendario"):
        reply = textwrap.dedent(f"""
        Aqui estão os últimos cinco jogos da FURIA e seus resultados:
        
        FURIA vs The MongolZ - quarta-feira, 9 de abril de 2025 - 0x2
        FURIA vs Virtus.pro - terça-feira, 8 de abril de 2025 - 0x2
        FURIA vs Complexity - segunda-feira, 7 de abril de 2025 - 1x2
        FURIA vs Apogee - domingo, 6 de abril de 2025 - 2x0
        M80 vs FURIA - sábado, 22 de março de 2025 - 2x1
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)

        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=["campeonatos"])
def championships(msg):

    if (last_main_command == "/calendario"):
        reply = textwrap.dedent(f"""
        Atualmente não foram anunciadas partidas oficialmente pela FURIA e quais próximos campeonatos irão participar.
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)

        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=["criacao"])
def born_when(msg):

    if (last_main_command == "/historico"):
        reply = textwrap.dedent(f"""
        A FURIA foi criada no ano de 2017, em São Paulo, por André Akkari, Jaime Pádua e Cris Guedes, como um time de Counter-Strike e já tendo um time com cinco jogadores e um técnico.
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)

        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=["ultimos_tecnicos"])
def last_coaches(msg):
    if (last_main_command == "/historico"):
        reply = textwrap.dedent(f"""
        Segue lista com os últimos técnicos (coaches) do time da FURIA de CS e suas datas de entrada e saída do time:
        
        Lucid (Hunter Tucker) - 09.07.2024 até 15.01.2025
        Inersh1ne (Viacheslav Britvin) - 09.07.2024 até 31.12.2024
        Sidde (Sidnei Macedo) - 16.01.2023 até 09.07.2024
        Guerri (Nicholas Nogueira ) - 02.02.2018 até 09.07.2024
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)

        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=["ultimos_jogadores"])
def last_players(msg):

    if (last_main_command == "/historico"):
        reply = textwrap.dedent(f"""
        Segue lista com os últimos jogadores do time da FURIA de CS e suas datas de entrada e saída do time:
        
        Skullz (Felipe Frank Medeiros) - 09/07/2024 até 22/04/2025
        chelo (Marcelo Cespedes) - 03/07/2023 até 11/04/2025
        kye (Kayke de Freitas) - 16/04/2024 até 12/05/2024
        ArT (Andrei Felipe Piovezan ) - 06/02/2018 até 16/04/2024
        Saffee (Rafael Innocencio) - 06/01/2022 até 28/06/2023
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)

        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=["competitions"])
def last_win_competitions(msg):

    if (last_main_command == "/historico"):
        reply = textwrap.dedent(f"""
        Segue lista com as últimas competições ganhas pelos times de CS da FURIA:
        
        1 - Aorus League – Brazil: Finals – Season 1 (2018)
        2 - ESL LA League Season 1 (2018)
        3 - Gamers Club Liga Profissional: Abril (2018)
        4 - GG.BET Ascensão (2018)
        5 - Aorus League – Invitational (2018)
        6 - Gamers Club Liga Profissional: Maio (2018)
        7 - ESL Brasil Premier League Season 5 (2018)
        8 - ESEA Season 30: Premier Division – NA (2019)
        9 - ESEA Season 31: Premier Division – NA (2019)
        10 - ESEA Season 31: Global Challenge (2019)
        11 - EMF CS:GO World Invitational (2019)
        12 - Arctic Invitational 2019 (2019)
        13 - BLAST Premier: Spring 2020 American Showdown (2020)
        14 - DreamHack Masters Spring NA (2020)
        15 - DreamHack Open Summer NA (2020)
        16 - ESL Pro League Season NA (2020)
        17 - IEM New York NA (2020)
        
        Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {last_main_command}
        """)

        bot.reply_to(msg, reply)


@bot.message_handler(commands=["time_e_jogadores"])
def teams_and_players(msg):
    global last_main_command
    last_main_command = "/time_e_jogadores"

    reply = textwrap.dedent(f"""
                Quem são os jogadores atuais do time de CS da FURIA? /jogadores
                Quem é o capitão do time de CS da FURIA? /capitao
                Quem é o coach (treinador) do time? /treinador
            """)

    bot.reply_to(msg, reply)
    
bot.message_handler(commands=["historico"])
def history(msg):
    global last_main_command
    last_main_command = "/historico"

    reply = textwrap.dedent(f"""
                Quando foi criado o time de CS da FURIA? /criacao
                Quem foram os ultimos jogadores do time? /ultimos_jogadores
                Quem foram os ultimos técnicos do time? /ultimos_tecnicos
                Quais títulos a FURIA ja conquistou com CS? /competitions
            """)

    bot.reply_to(msg, reply)

@bot.message_handler(commands=["calendario"])
def schedule(msg):
    global last_main_command
    last_main_command = "/calendario"

    reply = textwrap.dedent(f"""
                Quais os resultados dos ultimos jogos da FURIA? /resultados
                Quais os próximos campeonatos que devem rolar? /campeonatos
            """)

    bot.reply_to(msg, reply)

@bot.message_handler(commands=["start"])
def answer(msg):
    global last_main_command
    last_main_command = "/start"
    reply = textwrap.dedent(f"""
                Olá {msg.from_user.first_name}! Bem vindo ao bot de CS da FURIA!
                Sobre o que você quer saber?
                    
                Para saber sobre o time e jogadores, clique aqui /time_e_jogadores
                Para saber sobre calendário e próximos campeonatos, clique em /calendario
                Para saber sobre histórico e desempenho, clique em /historico
                Para saber alguma curiosidade aleatória sobre a gente? Então clique em /curiosidades    
            """)

    bot.reply_to(msg, reply)


@bot.message_handler(func=lambda msg: True)
def fallback_message(message):
    if (last_main_command == "" or last_main_command == "/start"):
        bot.reply_to(message, "Não entendi 😅. Para começar, digite /start.")
    else:
        bot.reply_to(
            message, f"Não entendi 😅. Voce gostaria de voltar para o inicio com /start ou prefere voltar ao ultimo menu com {last_main_command}")


bot.polling()
