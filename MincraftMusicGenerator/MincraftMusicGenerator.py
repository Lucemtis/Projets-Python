import random
from midiutil import MIDIFile

# Créer un objet MIDIFile avec deux pistes
MyMIDI = MIDIFile(2)

# Définir le tempo, le nombre de temps par mesure et la vitesse de la note
tempo = 120
time_signature = (4, 4)
duration = 1

# Ajouter des informations sur la piste et le tempo
MyMIDI.addTrackName(0, 0, "Random Melody")
MyMIDI.addTempo(0, 0, tempo)
MyMIDI.addTrackName(1, 0, "Chord Progression")
MyMIDI.addTempo(1, 0, tempo)

# Créer une liste de notes MIDI à partir desquelles choisir pour les accords
chord_notes = [(48, 52, 55), (50, 53, 57), (52, 55, 59), (53, 57, 60), (55, 59, 62), (57, 60, 64), (59, 62, 65), (60, 64, 67)]

# Générer des notes aléatoires et les ajouter à la piste MIDI pour la mélodie
for i in range(16):
    if i % 2 == 0:
        chord = random.choice(chord_notes)
    pitch = random.choice(chord) + 24
    if i % 2 == 0:
        duration = 2
    else:
        duration = 1
    MyMIDI.addNote(0, 0, pitch, i * duration, duration, random.randint(80, 100))

# Générer des accords aléatoires et les ajouter à la piste MIDI pour la progression d'accords
for i in range(16):
    if i % 2 == 0:
        chord = random.choice(chord_notes)
    duration = 2
    for j in range(len(chord)):
        MyMIDI.addNote(1, 0, chord[j], i * duration, duration, random.randint(40, 60))

# Écrire les données MIDI dans un fichier
with open("random_melody_with_chords_same_notes_with_rhythm_and_continuous_chords.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
