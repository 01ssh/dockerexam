FROM ubuntu:18.04

# Installation de Python 3 et des dépendances
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install flask==2.0.0 requests

# Définition du répertoire de travail
WORKDIR /app

