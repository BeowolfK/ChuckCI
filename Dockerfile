# Utiliser une image de base légère avec Node.js
FROM node:18-alpine
# Cloner un dépôt (à remplacer par l'URL de votre dépôt)
COPY . . 
RUN npm install
EXPOSE 8080
# Commande par défaut pour démarrer l'application
CMD ["npm", "start"]
