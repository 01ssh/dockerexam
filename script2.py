import os
import requests

# Définition de l'adresse de l'API
api_address = 'conteneur_api'
# Port de l'API
api_port = 8000

# Versions à tester
versions = ['v1', 'v2']

# Informations d'authentification pour Alice et Bob
alice_auth = ('alice', 'wonderland')
bob_auth = ('bob', 'builder')

# Fonction pour tester l'accès à chaque version pour chaque utilisateur
def test_access():
    for version in versions:
        # URL de la requête pour tester l'accès à la version spécifiée
        url = f'http://{api_address}:{api_port}/{version}/sentiment'
        
        # Effectue la requête avec les informations d'authentification d'Alice
        response_alice = requests.get(url, auth=alice_auth)
        # Affiche le résultat de la requête pour Alice
        print(f"============================")
        print(f"    Access test for Alice on {version}")
        print(f"============================")
        print(f"\nVersion: {version}")
        print(f"Status Code: {response_alice.status_code}")

        # Effectue la requête avec les informations d'authentification de Bob
        response_bob = requests.get(url, auth=bob_auth)
        # Affiche le résultat de la requête pour Bob
        print(f"============================")
        print(f"    Access test for Bob on {version}")
        print(f"============================")
        print(f"\nVersion: {version}")
        print(f"Status Code: {response_bob.status_code}")

# Appel de la fonction pour tester l'accès aux versions
test_access()

