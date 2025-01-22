from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_chuck = "https://api.chucknorris.io/jokes/random"
API_dog = "https://dog.ceo/api/breeds/image/random"

def call_chuck(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['value']
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Chuck Norris : {e}")

def call_dog(url): 
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['message']
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Dog CEO : {e}")

def call_translate(chuck_message, target_lang):
    source_lang = "en"
    api = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={chuck_message}"
    try:
        response = requests.get(api)
        response.raise_for_status()
        data = response.json()
        return data[0][0][0]
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Translate : {e}")
        return chuck_message

@app.route('/', methods=['GET', 'POST'])
def home():
    message_chuck = call_chuck(API_chuck)
    image_chien = call_dog(API_dog)
    selected_lang = request.form.get('language', 'fr')  # Default language is French
    translated_chuck = call_translate(message_chuck, selected_lang)
    return render_template('index.html', image_url=image_chien, texte=translated_chuck, selected_lang=selected_lang)

def main():
    app.run(host="0.0.0.0", port=8000, debug=False)

if __name__ == "__main__":
    main()
