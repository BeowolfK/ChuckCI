
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
   ```
   Accédez à l'application sur `http://localhost:8000` et vérifiez son fonctionnement.

---

