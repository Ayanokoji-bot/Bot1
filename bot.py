import os
from fbchat import Client, log
from fbchat.models import Message
from dotenv import load_dotenv
from flask import Flask

# Chargement des variables d'environnement
load_dotenv()

class JordanBot(Client):
    def __init__(self):
        super().__init__(os.getenv("FB_EMAIL"), os.getenv("FB_PASSWORD"))
    
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        # Votre logique de commandes
        if author_id == os.getenv("CREATOR_ID"):
            if "_mon serviteur" in message:
                self.send(Message(text="À vos ordres, mon empereur!"), 
                        thread_id=thread_id, 
                        thread_type=thread_type)

# Configuration Flask pour keep-alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Actif"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_flask).start()
    bot = JordanBot()
    bot.listen()
