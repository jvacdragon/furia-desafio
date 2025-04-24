import textwrap
from utils.state import set_last_command, get_last_command

def register(bot):
    @bot.message_handler(commands=["calendario"])
    def schedule(msg):
        set_last_command("/calendario")

        reply = textwrap.dedent(f"""
                    Quais os resultados dos ultimos jogos da FURIA? /resultados
                    Quais os próximos campeonatos que devem rolar? /campeonatos
                """)

        bot.reply_to(msg, reply)

    @bot.message_handler(commands=["campeonatos"])
    def championships(msg):

        if (get_last_command() == "/calendario"):
            reply = textwrap.dedent(f"""
            Atualmente não foram anunciadas partidas oficialmente pela FURIA e quais próximos campeonatos irão participar.
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
            """)

            bot.reply_to(msg, reply)
            
    @bot.message_handler(commands=["resultados"])
    def last_games(msg):

        if (get_last_command() == "/calendario"):
            reply = textwrap.dedent(f"""
            Aqui estão os últimos cinco jogos da FURIA e seus resultados:
            
            FURIA vs The MongolZ - quarta-feira, 9 de abril de 2025 - 0x2
            FURIA vs Virtus.pro - terça-feira, 8 de abril de 2025 - 0x2
            FURIA vs Complexity - segunda-feira, 7 de abril de 2025 - 1x2
            FURIA vs Apogee - domingo, 6 de abril de 2025 - 2x0
            M80 vs FURIA - sábado, 22 de março de 2025 - 2x1
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
            """)

            bot.reply_to(msg, reply)