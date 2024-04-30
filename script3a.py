import os
import requests


# définition de l'adresse de l'API
api_address = 'conteneur_api'
# port de l'API
api_port = 8000

# requête pour Alice
r = requests.get(
    url='http://{address}:{port}/v1/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
    Authentication test score  1
============================
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)


###########################

# requête pour Alice 
r = requests.get(
    url='http://{address}:{port}/v1/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
    Authentication test score 2
============================ 
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)


##################



# requête pour Alice 
r = requests.get(
    url='http://{address}:{port}/v2/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
Authentication test score 3
============================
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)

       
###########

 # requête pour Alice 
r = requests.get(
    url='http://{address}:{port}/v2/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
    Authentication test score 4
============================
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)

       
############


 # requête pour BOB 
r = requests.get(
    url='http://{address}:{port}/v2/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'bob',
        'password': 'builder',
        'sentence': 'life is beautiful'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
    Authentication test score 5
============================
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)


 # requête pour BOB 
r = requests.get(
    url='http://{address}:{port}/v2/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'bob',
        'password': 'builder',
        'sentence': 'that sucks'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
    Authentication test score 6
============================
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)

 # requête pour BOB 
r = requests.get(
    url='http://{address}:{port}/v1/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'bob',
        'password': 'builder',
        'sentence': 'life is beautiful'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
    Authentication test score 6
============================
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)

       
        # requête pour BOB 
r = requests.get(
    url='http://{address}:{port}/v1/sentiment/'.format(address=api_address, port=api_port),
    params={
        'username': 'bob',
        'password': 'builder',
        'sentence': 'that sucks'
    }
)

print("RESPONSE JSON:", r)
response = r.json()
score = response.get('score')
print("le score de la phrase", score)

output = '''
============================
    Authentication test score 7
============================
expected result = 200
actual result = {status_code}
==>  {test_status}
Score: {score}
'''

print(r.url)  # affichage de l'URL utilisée dans la requête

# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
#print(output.format(status_code=status_code, test_status=test_status, score=score, ))
output = output.format(score=score, test_status=test_status, status_code=status_code)
print(output)
# Vérifie si la variable d'environnement LOG est définie et a la valeur '1'
if os.environ.get('LOG') == '1':
    # Ouvre le fichier en mode d'ajout pour écrire le contenu
    with open('api_test.log', 'a') as file:
        # Écrit le contenu dans le fichier de journal
        file.write(output)
