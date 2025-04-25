import telebot
import textwrap
from utils.middleware_bot import StateMiddleware
from handlers import time_e_jogadores, calendarios, historico, curiosidades
from utils.state import set_last_command, get_last_command
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, use_class_middlewares=True)

bot.setup_middleware(StateMiddleware(bot))

time_e_jogadores.register(bot)
calendarios.register(bot)
historico.register(bot)
curiosidades.register(bot)
                
@bot.message_handler(commands=["start"])
def answer(msg):
    set_last_command("/start", None)
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
    bot.reply_to(message, "Não entendi 😅. Para iniciar o bot, digite /start.")


bot.polling()
