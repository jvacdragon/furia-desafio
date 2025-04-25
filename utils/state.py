_last_command = None
_current_subcommand = None

def set_last_command(command, subcommand=None):
    global _last_command, _current_subcommand
    _last_command = command
    _current_subcommand = subcommand

def get_last_command():
    return _last_command

def get_current_subcommand():
    return _current_subcommand