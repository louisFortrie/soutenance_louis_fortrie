# Dictionnaire de correspondance entre lettres/espaces et le code Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' / '  # Espace entre les mots
}

def translate_to_morse(text):
    return ' '.join(morse_code.get(char.upper(), '') for char in text)

# Exemple d'utilisation
input_text = 'Hello EEMI'
morse_text = translate_to_morse(input_text)
print('Hello EEMI en morse : ', morse_text)
