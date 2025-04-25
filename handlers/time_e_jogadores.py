import textwrap
from utils.state import set_last_command, get_last_command

def register(bot):
    
    @bot.message_handler(commands=["time_e_jogadores"])
    def teams_and_players(msg):
        set_last_command("/time_e_jogadores", None)
        reply = textwrap.dedent(f"""
                        Quem são os jogadores atuais do time de CS da FURIA? /jogadores
                        Quem é o capitão do time de CS da FURIA? /capitao
                        Quem é o coach (treinador) do time? /treinador
                    """)

        bot.reply_to(msg, reply)
        
    @bot.message_handler(commands=["capitao"])
    def leader(msg):
        set_last_command("/time_e_jogadores", "/capitao")
        reply = textwrap.dedent(f"""
            O capitão do time atualmente é o FalleN, responsável pelas estratégias e coordenação do time durante as partidas.
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
        """)
        bot.reply_to(msg,reply)
        
    @bot.message_handler(commands=["treinador"])
    def leader(msg):
        set_last_command("/time_e_jogadores", "/treinador")
        reply = textwrap.dedent(f"""
            Atualmente os treinadores do time são Sidde (Sidnei Macedo) e Heppa (Juan Borges), responáveis por estudar adversários, criarem táticas, dar feedbacks aos seus jogadores e preparar a equipe fora do servidor.
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
        """)
        bot.reply_to(msg, reply)


    @bot.message_handler(commands=["jogadores"])
    def players(msg):
        set_last_command("/time_e_jogadores", "jogador")
        reply = textwrap.dedent(f"""
            Atualmente os jogadores do time titular de CS FURIA são:
            
            KSCERATO - Kaike Cerato (Brasil)
            Yuurih - Yuri Boian (Brasil)
            FalleN - Gabriel Toledo (Brasil)
            Molodoi - Danil Golubenko (Cazaquistão)
            YEKINDAR - Mareks Gaļinskis (Letônia)
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
        """)

        bot.reply_to(msg, reply)