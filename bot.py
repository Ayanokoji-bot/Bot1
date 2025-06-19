import os
import logging
from fbchat import Client
from fbchat.models import Message
from dotenv import load_dotenv
from flask import Flask

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Chargement des variables d'environnement
load_dotenv()

class JordanBot(Client):
    def __init__(self):
        super().__init__(os.getenv("FB_EMAIL"), os.getenv("FB_PASSWORD"))
    
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        try:
            logger.info(f"Message reçu de {author_id}: {message}")
            
            if author_id == os.getenv("CREATOR_ID"):
                if "_mon serviteur" in message:
                    self.send(
                        Message(text="À vos ordres, mon empereur!"), 
                        thread_id=thread_id, 
                        thread_type=thread_type
                    )
        except Exception as e:
            logger.error(f"Erreur: {str(e)}")

# Configuration Flask pour keep-alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Actif"

def run_flask():
    app.run(host='0.0.0.0', port=
