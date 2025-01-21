import requests
from flask import Flask, render_template

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


def call_transalte(chuck_message):
    sourceLang = "en"
    tradLang = "fr"
    api = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sourceLang}&tl={tradLang}&dt=t&q={chuck_message}"

    try:
        response = requests.get(api)
        response.raise_for_status()
        data = response.json()
        return data[0][0][0]
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Translate : {e}")


@app.route('/')
def home():
    message_chuck = call_chuck(API_chuck)
    image_chien = call_dog(API_dog)
    fr_chuck = call_transalte(message_chuck)
    return render_template('index.html', image_url=image_chien, texte=fr_chuck)


def main():
    app.run(host="0.0.0.0", port="8080", debug=False)


if __name__ == "__main__":
    main()
