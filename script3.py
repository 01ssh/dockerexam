import requests

# Definition de l'adresse de l'API
api_address = 'conteneur_api'
# Port de l'API
api_port = 8000

# Phrases a tester
phrases = [
    "life is beautiful",
    "that sucks"
]

# Versions a tester
versions = ['v1', 'v2']

# Informations d'authentification pour Alice et Bob
alice_auth = ('alice', 'wonderland')
bob_auth = ('bob', 'builder')

# Fonction pour tester le contenu pour chaque utilisateur sur chaque version
def test_content():
    for phrase in phrases:
        for version in versions:
            # URL de la requete pour tester le contenu pour la version specifiee
            url = f'http://{api_address}:{api_port}/{version}/sentiment'
            # Effectue la requete avec les informations d'authentification d'Alice
            response_alice = requests.get(url, auth=alice_auth, params={'sentence': phrase})
            # Affiche le resultat de la requete pour Alice
            print("============================")
            print(f"    Content test for Alice on {version}")
            print("============================")
            print(f"\nPhrase: '{phrase}', Version: {version}")
            if response_alice.status_code == 200:
                score = response_alice.json().get('score')
                print(f"Score: {score}")
            else:
                print(f"Erreur '{phrase}' et la version {version}, Code de statut: {response_alice.status_code}")

            # Effectue la requete avec les informations d'authentification de Bob
            response_bob = requests.get(url, auth=bob_auth, params={'sentence': phrase})
            # Affiche le resultat de la requete pour Bob
            print("============================")
            print(f"    Content test for Bob on {version}")
            print("============================")
            print(f"\nPhrase: '{phrase}', Version: {version}")
            if response_bob.status_code == 200:
                score = response_bob.json().get('score')
                print(f"Score: {score}")
            else:
                print(f"Echec '{phrase}' et la version {version}, Code de statut: {response_bob.status_code}")

# Appel de la fonction pour tester le contenu
test_content()
