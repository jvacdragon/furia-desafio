import telebot
import textwrap
from handlers import time_e_jogadores, calendarios, historico
from utils.state import set_last_command, get_last_command
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

time_e_jogadores.register(bot)
calendarios.register(bot)
historico.register(bot)
                
@bot.message_handler(commands=["start"])
def answer(msg):
    set_last_command("/start")
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
    if (get_last_command() == "/start"):
        bot.reply_to(message, "Não entendi 😅. Para começar, digite /start.")
    else:
        bot.reply_to(
            message, f"Não entendi 😅. Voce gostaria de voltar para o inicio com /start ou prefere voltar ao ultimo menu com {get_last_command()}")


bot.polling()
