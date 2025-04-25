import random
import textwrap
from utils.state import set_last_command, get_last_command

def register(bot):
    
    curiosidades = ["Durante o IEM Rio Major 2022, a FURIA atingiu um pico de 1.428.993 espectadores simultâneos, estabelecendo um recorde de audiência para a equipe em torneios de CS. ​", "Desde sua estreia em 2018, a FURIA participou de mais de 550 partidas, com uma taxa de vitórias em torno de 60%. Eles competiram em aproximadamente 120 torneios, conquistando 19 títulos e recebendo convites diretos para quase metade deles.​", "Em 2021, a FURIA firmou o 'Acordo do Louvre' com a ESL, tornando-se uma parceira permanente da ESL Pro League. Esse acordo foi renovado até 2025, garantindo presença constante nos principais torneios da liga.", "A trajetória da FURIA no CO foi retratada no documentário ''FURIRoad to Legends', produzido pela Red Bull. O filme oferece uma visão dos bastidores e destaca a ascensão meteórica da equipe no cenário competitivo.", "molodoy, jovem talento do Cazaquistão, é a mais recente adição, trazendo uma nova perspectiva ao time.", "A FURIA está atualmente classificada como a 16ª melhor equipe do mundo, conforme o ranking da HLTV.", "A equipe se prepara para o PGL Astana 2025, que ocorrerá de 10 a 18 de maio em Astana, Cazaquistão, com uma premiação de $625.000.​", "KSCERATO e yuurih são os pilares da equipe, com mais de 1.300 mapas jogados cada e ratings acima de 1.17."]
    
    @bot.message_handler(commands=["curiosidades"])
    def curiosities(msg):
            set_last_command("/curiosidades", None)
            curiosity = random.choice(curiosidades)
            reply = textwrap.dedent(f"""
                                    {curiosity}
                                    
                                    Para mais curiosidades aleatórias clique em {get_last_command()} e caso queira voltar para o menu inicial, vá para /start
                                    """)
            bot.reply_to(msg, reply)