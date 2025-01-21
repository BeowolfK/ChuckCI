
# Projet ChuckCI

## Qu'est-ce que c'est ?
Chuck est une page permettant d'afficher une blague et uen image de chien en faisant appel à des APIs.

## Fonctionnalités d'intégration continue
- Exécute des workflows CI prédéfinis à l'aide de GitHub Actions.
- Prend en charge les déploiements basés sur Docker.

## Comment construire
1. **Installer les dépendances :**
   Assurez-vous d'avoir Python 3.8+ et Docker installés. Installez les bibliothèques Python requises avec :
   ```python
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Construire l'image Docker :**
   Créez l'image Docker à l'aide du `Dockerfile` fourni :
   ```python
   docker build -t chuckci .
   ```

## Comment tester
1. **Tests unitaires :**
   Exécutez le script de test Python pour valider la fonctionnalité des API :
   ```bash
   python test_api_calls.py
   ```

2. **Tests d'intégration :**
   Utilisez Docker pour tester le déploiement complet :
   ```bash
   docker run -p 8000:8000 chuckci

   
## Mise en Prod

```python
gunicorn -w 4 -b 0.0.0.0 'main:app'
```
   Accédez à l'application sur **http://localhost:8000** et vérifiez son fonctionnement.

## Description du Code

Ce projet Python utilise **Flask** pour servir une application web affichant une blague Chuck Norris traduite en français et une image aléatoire de chien. Le code repose sur trois APIs externes :

- **Chuck Norris API** : Fournit une blague aléatoire.
- **Dog CEO API** : Fournit une image aléatoire de chien.
- **Google Translate API** : Traduit la blague Chuck Norris de l'anglais au français.

### Fonctionnement :
1. Les blagues et les images sont récupérées via des appels HTTP (module `requests`).
2. Les données sont affichées sur une page HTML rendue à l'aide de Flask.
3. L'application s'exécute par défaut sur le port 8000.

### Structure du Code :
- `call_chuck(url)`: Récupère une blague depuis l'API Chuck Norris.
- `call_dog(url)`: Récupère une image aléatoire depuis l'API Dog CEO.
- `call_translate(chuck_message)`: Traduit une blague de l'anglais au français via l'API Google Translate.
- **Route principale** (`/`): Affiche la blague traduite et l'image de chien sur la page `index.html`.

Ce code est prêt pour un déploiement local ou basé sur un conteneur Docker et peut être facilement étendu.

