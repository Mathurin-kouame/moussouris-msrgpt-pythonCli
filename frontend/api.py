import requests
from rich import print
from .config import API_BASE
from .auth import load_token
import subprocess


def send_prompt(option: str= "Scan", prompt: str = None):
    token = load_token()

    if not token:
        print("[red]Vous n'etes pas connecté, retourne au menu pour se connecter[/]")
        exit()
     
    headers = {"Authorization": f"Bearer {token}"}

    try:
        reponse = requests.post(f"{API_BASE}/openai/chat", json={
            "option": option,
            "prompt": prompt
            }, headers=headers)

        if reponse.status_code == 200:
            limite_rep = reponse.json()["limite"]
            data_code = reponse.json()["data"]
            print(f"\n[bold green] {limite_rep} [/]")
            print("\n[bold cyan] Reponse à executer:  [/]", data_code)
            subprocess.run(data_code, shell=True)

        else:
            print("[bold red] Echec d'envoie[/]", reponse.text)
    except Exception as e:
            print("[bold red] Echec d'envoie[/]", e)
