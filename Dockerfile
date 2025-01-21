# Utiliser une image de base légère avec Node.js
FROM python:3.11-alpine
# Cloner un dépôt (à remplacer par l'URL de votre dépôt)
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 8080
CMD ["python3", "main.py"]
