import requests

def main(): 
    API_chuck = "https://api.chucknorris.io/jokes/random"
    API_dog = "https://dog.ceo/api/breeds/image/random"
    print("--- Appel de l'API Chuck Norris ---")
    message_chuck = call_chuck(API_chuck)

    print("\n--- Appel de l'API Dog CEO ---")
    url_picture_dog = call_dog(API_dog)

    url_translation = call_transalte(message_chuck)

def call_chuck(url): 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()
        print(f"Blague Chuck Norris : {data['value']}")
        return data['value']
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Chuck Norris : {e}")

def call_dog(url): 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()
        print(f"Image de chien : {data['message']}")
        return data['message']
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Dog CEO : {e}")

def call_transalte(chuck_message): 
    sourceLang = "en"
    tradLang = "fr"
    api=f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sourceLang}&tl={tradLang}&dt=t&q={chuck_message}"

    try:
        response = requests.get(api)
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()
        print(f"Traduction : {data[0][0][0]}")
        return data[0][0][0]
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Translate : {e}")

if __name__ == "__main__": 
    main()