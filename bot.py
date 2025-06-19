import fbchat
from fbchat import Client, Message
import time

class JordanBot(Client):
    def __init__(self, email, password):
        super().__init__(email, password)
    
    def onMessage(self, author_id, message, thread_id, **kwargs):
        # Vérifie si c'est le créateur
        if author_id == "100088171557555":  # Votre ID Facebook
            if "_mon serviteur" in message:
                self.handle_creator_command(message, thread_id)
        elif "-Ai" in message:
            self.handle_general_command(message, thread_id)
        
        # Autres fonctionnalités de modération...

# Configuration
bot = JordanBot("empereurmahamat@gmail.com", "monbotcompte235jordan")
bot.listen()
