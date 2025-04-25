from telebot.handler_backends import BaseMiddleware, CancelUpdate
from utils.state import get_last_command, get_current_subcommand

class StateMiddleware(BaseMiddleware):
    def __init__(self, bot):
        super().__init__()
        self.update_types = ['message']
        self.bot = bot
    
    def pre_process(self, msg, data):
        if not msg.text or not msg.text.startswith('/'):
            return
        
        user_input = msg.text.lower().strip()
        last_command = get_last_command()
        current_subcommand = get_current_subcommand()
        
        print(user_input, last_command, current_subcommand)
        
        if user_input == "/start":
            return
        
        command_rules = {
            "/calendario": {
                "allowed_subcommands": ["/campeonatos", "/resultados"],
                "allowed_commands": ["/start", "/calendario"]
            },
            
            "/curiosidades": {
                "allowed_subcommands": [],
                "allowed_commands": ["/start", "/curiosidades"]
            },
            
            "/historico": {
                "allowed_subcommands": ["criacao", "ultimos_tecnicos", "ultimos_jogadores", "competicoes"],
                "allowed_commands": ["/start", "/historico"]
            },
            
            "/time_e_jogadores": {
                "allowed_subcommands": ["/capitao", "/treinador", "/jogadores"],
                "allowed_commands": ["/start", "/time_e_jogadores"]
            }
        }
        
        if last_command == None:
            self.bot.reply_to(
                msg,
                f"Por favor, inicie o robô com o comando /start."
            )
            return CancelUpdate()
        
        if last_command == "/start" and user_input not in command_rules:
            print("NOVO IF")
            self.bot.reply_to(
                msg,
                f"⚠️ Comando {user_input} não identificado nas opções. Caso queira voltar para o inicio, clique em /start."
            )
            return CancelUpdate()
        
        if (
                (last_command in command_rules) and 
                (user_input not in command_rules[last_command]["allowed_subcommands"]) and 
                (user_input not in   command_rules[last_command]["allowed_commands"])
            ):
            print("IF 1")
            self.bot.reply_to(
                msg,
                f"⚠️ Você está no meio de {last_command}. Finalize ou cancele com /start antes de usar {user_input}."
            )
            return CancelUpdate()
        
        """ if current_subcommand and user_input not in command_rules[last_command]["allowed_subcommands"]:
            print("IF 2")
            self.bot.reply_to(
                msg,
                f"❌ Comando inválido. Você deve usar um subcomando de {last_command}."
            )
            return CancelUpdate() """
        
    def post_process(self, message, data, exception):
       pass
        