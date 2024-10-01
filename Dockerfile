# Utiliser Python 3.9 basé sur Debian (ou Slim pour une image plus légère)
FROM python:3.9-slim

# Mettre à jour les paquets et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    curl \
    libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier votre fichier requirements.txt dans l'image
COPY requirements.txt /app/requirements.txt

# Installer les dépendances Python à partir du requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de votre application dans le conteneur
COPY . /app

# Installer pytest
RUN pip install pytest

# Démarrer l'application
CMD ["python", "app.py"]
