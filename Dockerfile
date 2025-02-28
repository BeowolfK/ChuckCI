# Utiliser une image de base légère avec Node.js
FROM python:3.11-alpine
# Cloner un dépôt (à remplacer par l'URL de votre dépôt)
COPY . . 
# RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "main.py"]
