# Utiliser une image de base légère avec Node.js
FROM node:18-alpine
# Cloner un dépôt (à remplacer par l'URL de votre dépôt)
COPY . . 
EXPOSE 8080

