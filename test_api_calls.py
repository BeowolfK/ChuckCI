import pytest
from main import call_chuck, call_dog, call_transalte

API_chuck = "https://api.chucknorris.io/jokes/random"
API_dog = "https://dog.ceo/api/breeds/image/random"

def test_call_chuck():
    result = call_chuck(API_chuck)
    assert result is not None, "La réponse de l'API Chuck Norris est nulle"
    assert len(result) > 0, "La blague Chuck Norris est vide"

def test_call_dog():
    result = call_dog(API_dog)
    assert result is not None, "La réponse de l'API Dog est nulle"
    assert result.startswith("http"), "Le lien de l'image du chien est invalide"

def test_call_translate():
    test_message = "Chuck Norris a déjà compté jusqu'à l'infini. Deux fois."
    result = call_transalte(test_message)
    assert result is not None, "La réponse de l'API Translate est nulle"
    assert len(result) > 0, "Le texte traduit est vide"
