import os
import requests

# définition de l'adresse de l'API
api_address = 'conteneur_api'
# port de l'API
api_port = 8000

# requête pour Alice
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params={
        'username': 'alice',
        'password': 'wonderland'
    }
)

output = '''
============================
 Authentication test alice 1
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''
print(r.url)  # corrected to print the URL used in the request

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

output = output.format(test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)

# requête pour Bob
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params={
        'username': 'bob',
        'password': 'builder'
    }
)

output = '''
============================
 Authentication test bob 1
============================

request done at "/v1/sentiment"
| username="bob"
| password="builder"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

output = output.format(test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)

###################################V2

# requête pour bob
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params={
        'username': 'bob',
        'password': 'builder'
    }
)

output = '''
============================
 Authentication test bob 2
============================

request done at "/v2/sentiment"
| username="bob"
| password="builder"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

output = output.format(test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)

# requête pour Alice
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params={
        'username': 'alice',
        'password': 'wonderland'
    }
)

output = '''
============================
 Authentication test alice 2
============================

request done at "/v2/sentiment"
| username="bob"
| password="builder"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

output = output.format(test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)
