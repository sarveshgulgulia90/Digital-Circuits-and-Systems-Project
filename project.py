import pygame 
import time

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Function to convert text to Morse code
# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += '/' + ' '  # Use slash to represent space
    return morse_code


# Function to play Morse code with sound
def play_morse_code(morse_code):
    pygame.mixer.init()
    dot_length = 0.1  # Length of a dot in seconds
    dash_length = 3 * dot_length  # Length of a dash (3 times dot)
    space_length = dot_length  # Length of space between symbols
    word_space_length = 7 * dot_length  # Length of space between words

    for symbol in morse_code:
        if symbol == '.':
            pygame.mixer.Sound('dot.mp3').play()
            time.sleep(dot_length)
        elif symbol == '-':
            pygame.mixer.Sound('dash.mp3').play()
            time.sleep(dash_length)
        elif symbol == ' ':
            time.sleep(space_length)
        elif symbol == '/':
            time.sleep(word_space_length)

text = input("Enter text to convert to Morse code: ")
morse_code = text_to_morse(text)
print("Morse code:", morse_code)
play_morse_code(morse_code)
