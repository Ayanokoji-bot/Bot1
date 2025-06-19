from fbchat import Client
from fbchat.models import Message, ThreadType

EMAIL = "empereurmahamat@gmail.com"
PASSWORD = "monbotcompte235jordan"
CREATEUR = "Ëmpęręur Jordan inferno's"
ID_CREATEUR = "100088171557555"

class EmpereurBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        msg = message_object.text or ""

        if author_id == self.uid:
            return

        # Commandes spéciales du créateur
        if author_id == ID_CREATEUR and msg.startswith("_mon serviteur"):
            commande = msg[len("_mon serviteur"):].strip()

            if commande.startswith("vire"):
                cible = commande.split("vire", 1)[1].strip()
                self.send(Message(text=f"{cible} est viré (simulation)."), thread_id=thread_id, thread_type=thread_type)

            elif commande.startswith("réunion"):
                annonce = commande.split("réunion", 1)[1].strip()
                self.send(Message(text=f"📢 Réunion à {annonce}"), thread_id=thread_id, thread_type=thread_type)

        # Commandes générales
        elif msg.lower().startswith("-ai"):
            self.send(Message(text=f"🤖 Réponse IA : {msg[3:].strip()}"), thread_id=thread_id, thread_type=thread_type)

        # Message trop long
        elif len(msg.split()) > 100 and author_id != ID_CREATEUR:
            self.send(Message(text="⛔ Ce message est trop long et doit être validé par l’Empereur."), thread_id=thread_id, thread_type=thread_type)

        # Si on demande le créateur
        elif "qui est ton créateur" in msg.lower():
            self.send(Message(text=f"« Mon créateur est {CREATEUR}, le gangster le plus puissant du méta. »"), thread_id=thread_id, thread_type=thread_type)

client = EmpereurBot(EMAIL, PASSWORD)
client.listen()
