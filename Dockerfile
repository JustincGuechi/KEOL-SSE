# Utiliser une image de base Python
FROM python:3.13-slim

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-pip \
    python3-setuptools

# Définir le répertoire de travail dans le conteneur
WORKDIR /

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "Flask.py"]