import os
import re
import pyttsx3

# Chemin vers le dossier parent
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Chemin vers le fichier à ouvrir
transcription_f = os.path.join(parent_dir, "Voice_Traker", "transcription.txt")

# Chemin vers les scripts executables à ouvrir
GPT_f = os.path.join(parent_dir, "Executables", "GPT.py")

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

# Définir la fonction de réponse vocale
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Définition des actions à réaliser

def GPT():
    print("GPT")

def Youtube():
    print("Youtube")

def Google():
    print("Google")


with open(transcription_f) as transcript_file:
    Voice_txt = str(transcript_file.readline())

if "esclave" in Voice_txt:
        speak("Oui maitre")
        
        try:

            # Mapping de valeurs d'entrée à des fonctions correspondantes
            case_handlers = {
                "GPT": GPT,
                "j'ai pété": GPT,
                "j'ai peut-être": GPT,
                "Google": Google,
                "Youtube": Youtube,
            }

            # Chercher la chaine de caractère dans Voice_txt et case_handlers
            found = False
            for key in case_handlers.keys():
                if key.lower() in Voice_txt.lower():
                    case_handlers[key]()
                    found = True
                    break

            if not found:
                GPT()
        except:
            print("NONE")
