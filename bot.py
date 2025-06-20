from fbchat import Client
from fbchat.models import Message, ThreadType
import os
from dotenv import load_dotenv
from flask import Flask
import threading
import logging

# Configuration
logging.basicConfig(level=logging.INFO)
load_dotenv()

class EmpereurBot(Client):
    def __init__(self):
        super().__init__(os.getenv("FB_EMAIL"), os.getenv("FB_PASSWORD"))
        self.creator_id = os.getenv("ID_CREATEUR")
        self.creator_name = os.getenv("CREATEUR_NAME")

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        try:
            msg = message_object.text or ""

            if author_id == self.uid:
                return

            # Commandes du créateur
            if author_id == self.creator_id and msg.startswith("_mon serviteur"):
                self.handle_creator_commands(msg, thread_id, thread_type)
            
            # Commandes générales
            elif msg.lower().startswith("-ai"):
                self.send_ai_response(msg, thread_id, thread_type)
            
            # Modération
            elif len(msg.split()) > 100 and author_id != self.creator_id:
                self.moderate_long_message(thread_id, thread_type)
            
            # Identification
            elif "qui est ton créateur" in msg.lower():
                self.identify_creator(thread_id, thread_type)

        except Exception as e:
            logging.error(f"Erreur: {str(e)}")

    def handle_creator_commands(self, msg, thread_id, thread_type):
        commande = msg[len("_mon serviteur"):].strip()

        if commande.startswith("vire"):
            cible = commande.split("vire", 1)[1].strip()
            self.send(Message(text=f"{cible} est viré (simulation)."), 
                     thread_id=thread_id, 
                     thread_type=thread_type)

        elif commande.startswith("réunion"):
            annonce = commande.split("réunion", 1)[1].strip()
            self.send(Message(text=f"📢 Réunion à {annonce}"), 
                     thread_id=thread_id, 
                     thread_type=thread_type)

    def send_ai_response(self, msg, thread_id, thread_type):
        self.send(Message(text=f"🤖 Réponse IA : {msg[3:].strip()}"), 
                 thread_id=thread_id, 
                 thread_type=thread_type)

    def moderate_long_message(self, thread_id, thread_type):
        self.send(Message(text="⛔ Ce message est trop long et doit être validé par l'Empereur."), 
                 thread_id=thread_id, 
                 thread_type=thread_type)

    def identify_creator(self, thread_id, thread_type):
        self.send(Message(text=f"« Mon créateur est {self.creator_name}, le gangster le plus puissant du méta. »"), 
                 thread_id=thread_id, 
                 thread_type=thread_type)

# Configuration Flask pour keep-alive
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot Actif", 200

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    # Démarrer Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Démarrer le bot
    bot = EmpereurBot()
    bot.listen()
