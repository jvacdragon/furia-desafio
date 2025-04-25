from utils.state import set_last_command, get_last_command
import textwrap

def register(bot):
    @bot.message_handler(commands=["historico"])
    def history(msg):
        set_last_command("/historico", None)
        reply = textwrap.dedent(f"""
                        Quando foi criado o time de CS da FURIA? /criacao
                        Quem foram os ultimos jogadores do time? /ultimos_jogadores
                        Quem foram os ultimos técnicos do time? /ultimos_tecnicos
                        Quais títulos a FURIA ja conquistou com CS? /competicoes
                """)

        bot.reply_to(msg, reply)

    @bot.message_handler(commands=["criacao"])
    def born_when(msg):

        set_last_command("/historico", "/ciacao")
        reply = textwrap.dedent(f"""
            A FURIA foi criada no ano de 2017, em São Paulo, por André Akkari, Jaime Pádua e Cris Guedes, como um time de Counter-Strike e já tendo um time com cinco jogadores e um técnico.
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
        """)

        bot.reply_to(msg, reply)
            
    @bot.message_handler(commands=["ultimos_tecnicos"])
    def last_coaches(msg):
        set_last_command("/historico", "/ultimos_tecnicos")
        reply = textwrap.dedent(f"""
            Segue lista com os últimos técnicos (coaches) do time da FURIA de CS e suas datas de entrada e saída do time:
            
            Lucid (Hunter Tucker) - 09/07/2024 até 15/01/2025
            Inersh1ne (Viacheslav Britvin) - 09/07/2024 até 31/12/2024
            Sidde (Sidnei Macedo) - 16/01/2023 até 09/07/2024
            Guerri (Nicholas Nogueira ) - 02/02/2018 até 09/07/2024
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
        """)

        bot.reply_to(msg, reply)
            
    @bot.message_handler(commands=["ultimos_jogadores"])
    def last_players(msg):

        set_last_command("/historico", "/ultimos_jogadores")
        reply = textwrap.dedent(f"""
            Segue lista com os últimos jogadores do time da FURIA de CS e suas datas de entrada e saída do time:
            
            Skullz (Felipe Frank Medeiros) - 09/07/2024 até 22/04/2025
            chelo (Marcelo Cespedes) - 03/07/2023 até 11/04/2025
            kye (Kayke de Freitas) - 16/04/2024 até 12/05/2024
            ArT (Andrei Felipe Piovezan ) - 06/02/2018 até 16/04/2024
            Saffee (Rafael Innocencio) - 06/01/2022 até 28/06/2023
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
        """)

        bot.reply_to(msg, reply)
            
    @bot.message_handler(commands=["competicoes"])
    def last_win_competitions(msg):

        set_last_command("/historico", "/competicoes")
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
            
            Caso queira voltar para inicio, clique em /start e caso queira voltar para ultimo menu, clique em {get_last_command()}
        """)

        bot.reply_to(msg, reply)