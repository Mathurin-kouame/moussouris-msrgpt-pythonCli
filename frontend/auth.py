import requests
from rich import print
from .config import API_BASE, TOKEN_FILE
from getpass import getpass
import os




def register():
    print("[bold cyan]\n --- Création de compte ---[/]")
    fullname = input("Nom complet: ")
    pseudo = input("votre pseudo: ")
    email =  input("Email: ")
    password = getpass("Mot de passe: ")


    try:

        reponse = requests.post(f"{API_BASE}/auth/inscription", json={
            "fullName": fullname,
            "pseudo": pseudo,
            "email": email,
            "password": password
            })

        if reponse.status_code == 201:
            print("[green] compte crée avec succès. vous pouvez maintenant vous connecter.[/]")
        else:
            print("[red]Erreur: Inscription avorté[/]",reponse.json().get('message', 'Erreur inconnue'))
    except Exception as e:
        print("[red]Erreur de connexion : [/]", e)
    

def login():
    print("[bold cyan]\n ___ se connecter ___[/]")
    email = input("votre Email: ")
    password = getpass("votre mot de passe: ")

    try: 
        reponse = requests.post(f"{API_BASE}/auth/connexion", json={
                "email": email,
                "password": password
                })

        if reponse.status_code == 200:
            token = reponse.json()['token']
            save_token(token)
            print("[green]Connexion reussie.[/]")
        else:
            print("[red]Erreur: connexion echoue[/]",reponse.json().get('message', 'Erreur inconnue'))

    except Exception as e:
        print("[red]Erreur de connexion au serveur :[/]", e)

def logout():
      print("[bold cyan]\n __ se deconnecter __[/]")
      

def save_token(token):
    with open(TOKEN_FILE, 'w') as f:
        f.write(token)
 
def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip()
