import requests

MORSE_API_URL = 'https://api.funtranslations.com/translate/morse.json'

params = {
    'text': input('Enter your text to convert to morse code:\n> ')
}

response = requests.get(MORSE_API_URL, params=params)
translated = response.json()['contents']['translated']
print(f"Your translated text is: {translated}")