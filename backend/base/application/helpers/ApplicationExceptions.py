
class ApplicationExceptions:
    
    def CommandException(message):
        return Exception("command", message)