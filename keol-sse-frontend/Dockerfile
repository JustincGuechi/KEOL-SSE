# Étape 1 : Construire l'application React
FROM node:16 AS build

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers package.json et package-lock.json
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers de l'application
COPY . .

# Construire l'application pour la production
RUN npm run build

# Étape 2 : Servir l'application avec nginx
FROM nginx:alpine

# Ajouter une étiquette pour identifier l'image du frontend
LABEL app=frontend

# Copier les fichiers construits de l'étape précédente
COPY --from=build /app/build /usr/share/nginx/html

# Copier la configuration nginx personnalisée
COPY default.conf /etc/nginx/conf.d/default.conf

# Exposer le port sur lequel nginx va écouter
EXPOSE 80

# Démarrer nginx
CMD ["nginx", "-g", "daemon off;"]