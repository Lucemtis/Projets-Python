def clear_transcription():
    with open('transcription.txt', 'w') as f:
        f.truncate(0)

def write_transcription(text):
    clear_transcription()
    with open('transcription.txt', 'w') as f:
        f.write(text)

text = input('Entrez votre message : ')
write_transcription(text)
