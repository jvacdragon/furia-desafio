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
        Atualmente os jogadores de CS da Furia são:
        
        KSCERATO - Kaike Cerato (Brasil)
        Yuurih - Yuri Boian (Brasil)
        FalleN - Gabriel Toledo (Brasil)
        Molodoi - Danil Golubenko (Cazaquistão)
        YEKINDAR - Mareks Gaļinskis (Letônia)
        
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


@bot.message_handler(commands=["start"])
def answer(msg):
    global last_main_command
    last_main_command = "/start"
    reply = textwrap.dedent(f"""
                Olá {msg.from_user.first_name}! Bem vindo ao bot de CS da Furia!
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
