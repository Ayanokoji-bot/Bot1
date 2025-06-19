import fbchat
from fbchat import Client
from fbchat.models import Message

class JordanBot(Client):
    def __init__(self, email, password, session_cookies=None):
        # Nouvelle syntaxe pour fbchat v2.0+
        super().__init__(email, password, session_cookies=session_cookies)
    
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        if author_id == "100088171557555":  # Votre ID Facebook
            if "_mon serviteur" in message:
                self.handle_creator_command(message, thread_id, thread_type)
        elif "-Ai" in message:
            self.handle_general_command(message, thread_id, thread_type)

# Initialisation correcte
bot = JordanBot(
    email="empereurmahamat@gmail.com",
    password="monbotcompte235jordan"
)
bot.listen()
