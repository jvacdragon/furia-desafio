_last_command = "/start"

def set_last_command(command):
    global _last_command
    _last_command = command

def get_last_command():
    return _last_command