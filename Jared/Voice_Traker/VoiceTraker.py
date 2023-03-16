import speech_recognition as sr
import os

# Créer une instance de la classe Recognizer
r = sr.Recognizer()
r.dynamic_energy_threshold = True
dB = 30
r.energy_threshold = 10 ** (dB / 20)
max_time_phrase = 15 # temps max des phrases

# Chemin vers le dossier parent
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Chemin vers le fichier à ouvrir
config_f = os.path.join(parent_dir, "Voice_Traker", "config.txt")
VoiceDistribSCR_f = os.path.join(parent_dir, "Voice_Traker", "VoiceDistribSCR.py")
transcription_f = os.path.join(parent_dir, "Voice_Traker", "transcription.txt")

# Charger la configuration du microphone s'il existe
try:
    with open(config_f) as config_file:
        mic_index = int(config_file.readline())
except:
    mic_index = None

# Boucle de sélection du microphone
while True:
    if mic_index is None:
        print("Aucun microphone n'est configuré.")

        # Liste des microphones disponibles
        print("Liste des microphones disponibles :")
        for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"{i} : {mic_name}")

        # Demander à l'utilisateur de choisir un microphone
        choice = input("Entrez le numéro du microphone que vous souhaitez utiliser : ")

        # Vérifier si le choix est valide
        try:
            mic_index = int(choice)
            mic = sr.Microphone(device_index=mic_index)
            with mic as source:
                r.adjust_for_ambient_noise(source)
            break
        except ValueError:
            print("Entrée invalide. Veuillez saisir un numéro valide.")

        except sr.RequestError:
            print("Le microphone n'est pas disponible. Veuillez en choisir un autre.")

    else:
        print(f"Microphone sélectionné : {sr.Microphone.list_microphone_names()[mic_index]}")
        
        break

        
while True:

    # Utiliser le microphone sélectionné
    with sr.Microphone(device_index=mic_index) as source:
        print("Dites quelque chose :")
        audio = r.listen(source, phrase_time_limit=max_time_phrase)

    try:
        transcribed_text = r.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + transcribed_text)

        with open(transcription_f, "w") as f:
            f.write(transcribed_text)

        exec(open(VoiceDistribSCR_f).read())

    except sr.UnknownValueError:
        print("En attente")
    except sr.RequestError as e:
        print("Erreur de transcription : {0}".format(e))

    # # Demander à l'utilisateur s'il souhaite continuer
    # choice = input("Voulez-vous continuer à enregistrer la voix? (o/n)")
    # if choice.lower() == "n":
    #     break

# Enregistrer l'index du microphone sélectionné dans un fichier de configuration
with open(config_f, "w") as config_file:
    config_file.write(str(mic_index))

print("Transcription terminée avec succès.")
